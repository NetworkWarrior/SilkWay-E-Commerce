class Cart():

    def __init__(self, request):
         
        self.session = request.session

        # returnin user obtainig his/her existing session

        cart = self.session.get('session_key')

        # new user generationg a new session 

        if 'session_key' not in request.session:
              
              cart = self.session['session_key'] = {}

        self.cart = cart