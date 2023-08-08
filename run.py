import sys
import logging

from aiohttp.web import run_app

from sqli.app import init as init_app

# AWS_ACCESS_KEY_ID="AKIAJAA49FFSFRFN6AAA" 
# AWS_SECRET_ACCESS_KEY="u9N1o8s+u3q4uwt9s8dfsdf/afx/d/24449YiNHN"

log = logging.getLogger(__name__)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(sys.argv[1:])

    host = app['config']['app']['host']
    port = app['config']['app']['port']
    log.info(f'App is listening at http://{host}:{port}')
    run_app(app, host=host, port=port)
