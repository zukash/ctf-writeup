const app = require("fastify")();
const PORT = 3000;

app.register(require("@fastify/http-proxy"), {
  upstream: "http://backend:3000",
  preValidation: async (req, reply) => {
    // WAF???
    try {
      console.log("[body, type] " + req.body + " " + typeof req.body);
      console.log("[header] %j", req.headers);
      const body =
        typeof req.body === "object" ? req.body : JSON.parse(req.body);
      // console.log("[body] " + body + " " + typeof body);
      console.dir(body, { depth: null });

      if ("givemeflag" in body) {
        reply.send("🚩");
      }
    } catch {}
  },
  replyOptions: {
    rewriteRequestHeaders: (_req, headers) => {
      console.log(headers);
      headers["content-type"] = "application/json";
      return headers;
    },
  },
});

app.listen({ port: PORT, host: "0.0.0.0" });
