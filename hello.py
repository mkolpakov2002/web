def hello_func(env, start_response):
    
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    start_response(status, headers)
    
    body = [bytes(q + '\n', 'ascii') for q in env['QUERY_STRING'].split('&')]
    return body
