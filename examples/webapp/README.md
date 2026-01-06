# REST-RPC – Web App Example

This is a small example for a web app that is written with the help of REST-RPC and [PyScript](https://pyscript.net/).

Here, the complete front-end is located inside the `static` directory. The front-end logic is inside `static/main.py`. Since the `static/pysript.toml` contains `rest-rpc` as a dependency, it is automatically installed from PyPI. `static/my_api.py` on the other hand is symlinked from `./my_api.py`.

Inside `./main.py`, you'll find that the FastAPI app that is auto-generated from REST-RPC via `api_impl.make_fastapi()` is re-routed to `/api` and that `/` points to the `static` directory. This means that you'll find the `read_item` method under `/api/items/{item_id}` instead of simply `/items/{item_id}`. This has to be considered by the front-end: Here, we are using `ApiClient(..., base_url="/api/")`.

By the way, if you want to use Pyodide without Pyscript, you can do that too. In this example, you can see for yourself that you can also use `engine="pyodide"` and it will still work (since PyScript uses Pyodide internally here). So you can simply install REST-RPC inside your Pyodide environment.

## Usage

To start the FastAPI server, simply run
```shell
$ uv run fastapi dev
```

You should now be able to open `http://127.0.0.1:8000` in your webbrowser and see the web app.

When clicking on the button, you should get an alert with the API response.

If the app is hanging in the "Loading..." screen, something might be wrong with your internet connection or with PyScript's CDN.

## Structure

- `my_api.py`: Api definition (shared between back-end and front-end)
- `main.py`: FastAPI back-end
- `static/index.html`: Front-end HTML
- `static/main.py`: Front-end logic implemented with PyScript

