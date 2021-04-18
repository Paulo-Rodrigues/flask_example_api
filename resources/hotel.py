from flask_restful import Resource, Api

hoteis = [{'hotel_id': '1', 'name': 'first hotel'}]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'not found'}, 404


    def post(self, hotel_id):
        args = reqparse.RequestParser()
        args.add_argument('name')
        
        data = args.parse_args()

        new_hotel = {'hotel_id': hotel_id, 'name': data['name']}
        
        hoteis.append(new_hotel)
        return new_hotel, 201

    def put(self, hotel_id):
        pass

    def delete(self, hotel_id):
        pass
