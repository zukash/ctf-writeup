package main

import (
	"net/http"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"fmt"

	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

func main() {
	r := gin.Default()
	r.LoadHTMLGlob("templates/*")

	r.MaxMultipartMemory = 1 << 20 // 1MiB, to prevent DoS

	r.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "index.html", gin.H{
			"result": "",
		})
	})

	r.POST("/", func(c *gin.Context) {
		baseDir := filepath.Join("/tmp", uuid.NewString()) // ex. /tmp/02050a65-8ae8-4b50-87ea-87b3483aab1e
		zipPath := baseDir + ".zip"                        // ex. /tmp/02050a65-8ae8-4b50-87ea-87b3483aab1e.zip
		fmt.Println(baseDir)

		file, err := c.FormFile("file")
		fmt.Println(file)
		if err != nil {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : " + err.Error(),
			})
			return
		}

		extractTarget := c.PostForm("target")
		fmt.Println(extractTarget)
		if extractTarget == "" {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : target is required",
			})
			return
		}

		if err := os.MkdirAll(baseDir, 0777); err != nil {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : " + err.Error(),
			})
			return
		}

		if err := c.SaveUploadedFile(file, zipPath); err != nil {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : " + err.Error(),
			})
			return
		}

		if err := ExtractFile(zipPath, baseDir); err != nil {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : " + err.Error(),
			})
			return
		}

		result, err := ExtractContent(baseDir, extractTarget)
		if err != nil {
			c.HTML(http.StatusOK, "index.html", gin.H{
				"result": "Error : " + err.Error(),
			})
			return
		}

		c.HTML(http.StatusOK, "index.html", gin.H{
			"result": result,
		})
	})

	if err := r.Run(":8080"); err != nil {
		panic(err)
	}
}

func ExtractFile(zipPath, baseDir string) error {
	if err := exec.Command("unzip", zipPath, "-d", baseDir).Run(); err != nil {
		return err
	}
	return nil
}

func ExtractContent(baseDir, extractTarget string) (string, error) {
	fmt.Println(baseDir, extractTarget, filepath.Join(baseDir, extractTarget))
	raw, err := os.ReadFile(filepath.Join(baseDir, extractTarget))
	if err != nil {
		return "", err
	}

	removeXmlTag := regexp.MustCompile("<.*?>")
	resultXmlTagRemoved := removeXmlTag.ReplaceAllString(string(raw), "")
	removeNewLine := regexp.MustCompile(`\r?\n`)
	resultNewLineRemoved := removeNewLine.ReplaceAllString(resultXmlTagRemoved, "")
	return resultNewLineRemoved, nil
}
