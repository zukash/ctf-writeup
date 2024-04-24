rule hoge {
    strings:
        $shebang = /^ctf4b.*/
    condition:
        $shebang
}
rule shebang {
    strings:
        $shebang = /^#!(\/[^\/ ]*)+\/?/
    condition:
        $shebang
}
rule maybe_python_executable {
    strings:
        $ident = /python(2|3)\r*\n/
    condition:
        shebang and $ident
}
