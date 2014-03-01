import sae
import web

'''def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, response_headers)
    return ['<strong>Welcome to SAE!</strong>']'''

def app(environ, start_response):
	status = '200 OK'
	response_headers = [('Content-type', 'text/html; charset=utf-8')]
	start_response('301 Redirect', [('Location', 'static/index.html'),])
	return ['<script language="javascript">window.navigate("static/index.html");</script>']

application = sae.create_wsgi_app(app)