from flask_restful import Resource, Api

hoteis = [{'hotel_id': '1', 'name': 'first hotel'}]

class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}


class Hotel(Resource):
    args = reqparse.RequestParser()
    args.add_argument('name')

    def get(self, hotel_id):
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            return hotel
        return { 'message': 'not found' }, 404

    def post(self, hotel_id):
        data = Hotel.args.parse_args()

        new_hotel = {'hotel_id': hotel_id, 'name': data['name']}
        
        hoteis.append(new_hotel)
        return new_hotel, 201

    def put(self, hotel_id):
        dados = Hotel.args.parse_args()

        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(new_hotel)
        return { 'message': 'not found' }, 404

    def delete(self, hotel_id):
        pass

    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'message': 'not found'}, 404
