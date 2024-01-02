import json
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
def air_request_1(request):
    
    data =  json.loads(open('parcing/data.json', "r").read() ) 
    xx = []

    alls = data['AirFareSearchResponse']['PricedItineraries']['Flights']


    for x in alls:
        counnt = len(x['OnwardPricedItinerary']['Flights']['Flight'])
        if counnt == 2 :
            x1 = x['OnwardPricedItinerary']['Flights']['Flight'][0]['Source']
            x2 = x['OnwardPricedItinerary']['Flights']['Flight'][1]['Destination']
            if x1 == request.GET.get('q1') and x2 == request.GET.get('q2'):
                json_name =  x['OnwardPricedItinerary']['Flights']['Flight'][0]['Carrier']['#text']
                Flight = { 
                    'Arrive-1': x['OnwardPricedItinerary']['Flights']['Flight'][0]  ,
                    'Arrive-2': x['OnwardPricedItinerary']['Flights']['Flight'][1]  ,
                    'Return-1': x['ReturnPricedItinerary']['Flights']['Flight'][0]  ,
                    'Return-2': x['ReturnPricedItinerary']['Flights']['Flight'][1]  ,
                    'Pricing': x['Pricing']['ServiceCharges'][2]['#text'] ,
                        }


                xx.append({ json_name: Flight })
        elif counnt == 11 :
            x1 = x['OnwardPricedItinerary']['Flights']['Flight']['Source']
            x2 = x['OnwardPricedItinerary']['Flights']['Flight']['Destination']
            if x1 == request.GET.get('q1') and x2 == request.GET.get('q2'):
                json_name = x['OnwardPricedItinerary']['Flights']['Flight']['Carrier']['#text']
                Flight = {
                    'Arrive-1': x['OnwardPricedItinerary']['Flights']['Flight']  ,
                    'Return-1': x['ReturnPricedItinerary']['Flights']['Flight'] ,
                    'Pricing': x['Pricing']['ServiceCharges'][2]['#text'],
                        }
                xx.append({json_name: Flight})

        
    json_data = json.dumps(xx, indent=4 , sort_keys=False)
    optimal = len(xx) / 2

    if request.GET.get('pricing') == 'expensive':
        expensive = json.loads(json_data)[int(len(xx)) -1]
        return Response(expensive , status=200 )
    elif request.GET.get('pricing') == 'cheap':
        cheap = json.loads(json_data)[0]
        return Response(cheap , status=200 )
    elif request.GET.get('pricing') == 'average':
        average = json.loads(json_data)[int(optimal)]
        return Response(average , status=200 )

    return Response(json.loads(json_data) , status=200 )


@api_view(['GET'])
def air_request_2(request):

    data =  json.loads(open('parcing/data.json', "r").read() ) 
    xx = []

    alls = data['AirFareSearchResponse']['PricedItineraries']['Flights']


    for x in alls:
        counnt = len(x['OnwardPricedItinerary']['Flights']['Flight'])
        if counnt == 2 :
            x1 = x['OnwardPricedItinerary']['Flights']['Flight'][0]['Source']
            x2 = x['OnwardPricedItinerary']['Flights']['Flight'][1]['Destination']
            if x1 == request.GET.get('q1') and x2 == request.GET.get('q2'):
                json_name =  x['OnwardPricedItinerary']['Flights']['Flight'][0]['Carrier']['#text']
                Flight = { 
                    'Arrive-1': x['OnwardPricedItinerary']['Flights']['Flight'][0]  ,
                    'Arrive-2': x['OnwardPricedItinerary']['Flights']['Flight'][1]  ,
                    'Pricing': x['Pricing']['ServiceCharges'][2]['#text'] ,
                        }


                xx.append({ json_name: Flight })
        elif counnt == 11 :
            x1 = x['OnwardPricedItinerary']['Flights']['Flight']['Source']
            x2 = x['OnwardPricedItinerary']['Flights']['Flight']['Destination']
            if x1 == request.GET.get('q1') and x2 == request.GET.get('q2'):
                json_name = x['OnwardPricedItinerary']['Flights']['Flight']['Carrier']['#text']
                Flight = {
                    'Arrive-1': x['OnwardPricedItinerary']['Flights']['Flight']  ,
                    # 'Return-1': x['ReturnPricedItinerary']['Flights']['Flight'] ,
                    'Pricing': x['Pricing']['ServiceCharges'][2]['#text'],
                        }
                xx.append({json_name: Flight})

        
    json_data = json.dumps(xx, indent=4 , sort_keys=False)
    optimal = len(xx) / 2

    if request.GET.get('pricing') == 'expensive':
        expensive = json.loads(json_data)[int(len(xx)) -1]
        return Response(expensive , status=200 )
    elif request.GET.get('pricing') == 'cheap':
        cheap = json.loads(json_data)[0]
        return Response(cheap , status=200 )
    elif request.GET.get('pricing') == 'average':
        average = json.loads(json_data)[int(optimal)]
        return Response(average , status=200 )

    return Response(json.loads(json_data) , status=200 )
