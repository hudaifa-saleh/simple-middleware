class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print("Some one visits the website")
        response = self.get_response(request)
        return response
