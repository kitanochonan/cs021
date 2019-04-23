    flights = {'Burlington':['Boston', 'New York', 'Los Angeles'],'New York': ['Los Angeles', 'Fort Lauderdale','Boston'],'Boston' : ['Montreal','Memphis','Washington'],'Washington' : ['Boston', 'San Diego'],'Los Angeles' : ['San Diego', 'Boston', 'Washington'],'Montreal': ['Boston','Fort Lauderdale'],'Fort Lauderdale' : ['Boston', 'Montreal'],'Memphis': ['Boston'],'San Diego': ['Los Angeles', 'Washington']}

    airport = str(input("AIRPORT? ")).lower().capitalize()
    if airport in flights:
        dct_cities = flights.get(airport, "Couldn't find the airport.")
        for city in dct_cities:
            print(city, "direct")
            via_city = flights[city]
            for viaCity in via_city:
                print(viaCity, "via", city)
    else:
        print("Couldn't find the airport.")

main()
