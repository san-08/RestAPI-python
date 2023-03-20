import cherrypy
import json

class ItemAPI:
    def __init__(self):
        self.data = json.load(open('data.json'))
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return self.data
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def get_item(self):
        for item in self.data['items']:
                return item
        return {'error': 'Item not found'}
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()

    def post_item(self):
        item = cherrypy.request.json
        item['Server_id'] = len(self.data['items']) + 1
        self.data['items'].append(item)
        json.dump(self.data, open('data.json', 'w'))
        return item
    
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()

    def put_item(self, id):
        for item in self.data['items']:
            if item['Server_id'] == int(id):
                updated_item = cherrypy.request.json
                item.update(updated_item)
                json.dump(self.data, open('data.json', 'w'))
                return item
        return {'error': 'Item not found'}
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def delete_item(self, id):
        for item in self.data['items']:
            if item['Server_id'] == int(id):
                self.data['items'].remove(item)
                json.dump(self.data, open('data.json', 'w'))
                return {'message': 'Item deleted'}
        return {'error': 'Item not found'}

if __name__ == '__main__':
    cherrypy.quickstart(ItemAPI())
