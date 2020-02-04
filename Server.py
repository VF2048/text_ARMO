import tornado.ioloop
import tornado.web

import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # python-3.8.0a4

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Response from server!")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen( 8888 )
    tornado.ioloop.IOLoop.current().start()

