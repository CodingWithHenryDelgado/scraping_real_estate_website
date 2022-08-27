import requests
import pandas as pd
import sqlalchemy

headers = {
    'authority': 'api2.realtor.ca',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'accept': '*/*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.realtor.ca',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.realtor.ca/',
    'accept-language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7',
    'cookie': 'visid_incap_2269415=pjB3DImWSy2DSncBmJhxAdFrDWEAAAAAQUIPAAAAAABjsqrQxZ4W1Wnwofq2RdhC; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=AcUYRjx+RSySjRa8AwANG+RrDWEAAAAAQUIPAAAAAABz1Fko5zVbdsXy74RazGys; nlbi_2269415=Em8eFcjFeXL+7IQPkG5lugAAAADPg2wjkaj3uQSIwXxK4Cjd; incap_ses_1343_2269415=kd1PX+Cf0BhALs9dmkujEkxgDmEAAAAAUvek0Memst9B9aq/AcYj4w==; incap_ses_259_2269415=jnQudMVXKnK+XGpiLCeYA01gDmEAAAAA8A3p2AjZwv8Q1Zh2MaB8mw==; ASP.NET_SessionId=glpnlclmpz50wotgeqehu4jr; nlbi_2271082=SfEKDy6GbC4XWhkacbDG1QAAAABjVV7rSMCr/IMzx8nZxG8I; incap_ses_259_2271082=va17EetpSBS+ZGpiLCeYA1ZgDmEAAAAASC01QSktKpD62+V0kmI30Q==; nlbi_2269415_2147483646=O/A+S2g5U0ZQz+i0kG5lugAAAACHpPSMoaIU04ye5O/9KPg+; reese84=3:6um7YNgYz8C3YlgtKUywaQ==:g+sd2OuCy9k/8A6ZrTnAIF0PEOiOQ63KvC3AXenvcxFEX0tefMKwOLinaH3sBe/qSd1Cp39gxrnEZYzCTwjirA1giIrHZ8AIBFzOQdgS8IIvgLiyqca5AQJkn/uTUMBfI67AIEa9R76y02XdWOv9J1oL38idnsS5t2D64eVSOuDMaiGKk081I7fKqpKfzTgN6GipRG45Jep9y19J4ypRkAtUvTa5X1XqYMDfeDsll8RBGCk9C8G51Zn9oYLl1P3Q2m26tXINwMyLMqk9rZUiDF2a1rRmZVyAgWgd9VOfoqTkEwSLl5xasgi0kWm4+G4abFGR1F4ivO+aX0d5aLc6g8/krH+S2COydjRF2KyToWVZZpNXYrIDOxVt0CW4Tyh55k3GyrlePPKMKA0WKoklfZh7jWYwkYYix4c/CjMvpEA=:fI0KfucP5l7cl5S+11F0HubnNJi8hSNbWALShpW3Lcw=',
}

data = {
    'LatitudeMax': '45.53758',
    'LongitudeMax': '-75.24660',
    'LatitudeMin': '44.96273',
    'LongitudeMin': '-76.35392',
    'Sort': '6-D',
    'PropertyTypeGroupID': '1',
    'PropertySearchTypeId': '1',
    'TransactionTypeId': '2',
    'Currency': 'CAD',
    'RecordsPerPage': '12',
    'ApplicationId': '1',
    'CultureId': '1',
    'Version': '7.0',
    'CurrentPage': '1'
}

response = requests.post(
    'https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)

response_json = response.json()

response_json.keys()

for i in range(1, 51):

    headers = {
        'authority': 'api2.realtor.ca',
        'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
        'accept': '*/*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.realtor.ca',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.realtor.ca/',
        'accept-language': 'en-US,en;q=0.9,de-DE;q=0.8,de;q=0.7',
        'cookie': 'visid_incap_2269415=pjB3DImWSy2DSncBmJhxAdFrDWEAAAAAQUIPAAAAAABjsqrQxZ4W1Wnwofq2RdhC; gig_bootstrap_3_mrQiIl6ov44s2X3j6NGWVZ9SDDtplqV7WgdcyEpGYnYxl7ygDWPQHqQqtpSiUfko=gigya-pr_ver4; visid_incap_2271082=AcUYRjx+RSySjRa8AwANG+RrDWEAAAAAQUIPAAAAAABz1Fko5zVbdsXy74RazGys; nlbi_2269415=Em8eFcjFeXL+7IQPkG5lugAAAADPg2wjkaj3uQSIwXxK4Cjd; incap_ses_1343_2269415=kd1PX+Cf0BhALs9dmkujEkxgDmEAAAAAUvek0Memst9B9aq/AcYj4w==; incap_ses_259_2269415=jnQudMVXKnK+XGpiLCeYA01gDmEAAAAA8A3p2AjZwv8Q1Zh2MaB8mw==; ASP.NET_SessionId=glpnlclmpz50wotgeqehu4jr; nlbi_2271082=SfEKDy6GbC4XWhkacbDG1QAAAABjVV7rSMCr/IMzx8nZxG8I; incap_ses_259_2271082=va17EetpSBS+ZGpiLCeYA1ZgDmEAAAAASC01QSktKpD62+V0kmI30Q==; nlbi_2269415_2147483646=O/A+S2g5U0ZQz+i0kG5lugAAAACHpPSMoaIU04ye5O/9KPg+; reese84=3:6um7YNgYz8C3YlgtKUywaQ==:g+sd2OuCy9k/8A6ZrTnAIF0PEOiOQ63KvC3AXenvcxFEX0tefMKwOLinaH3sBe/qSd1Cp39gxrnEZYzCTwjirA1giIrHZ8AIBFzOQdgS8IIvgLiyqca5AQJkn/uTUMBfI67AIEa9R76y02XdWOv9J1oL38idnsS5t2D64eVSOuDMaiGKk081I7fKqpKfzTgN6GipRG45Jep9y19J4ypRkAtUvTa5X1XqYMDfeDsll8RBGCk9C8G51Zn9oYLl1P3Q2m26tXINwMyLMqk9rZUiDF2a1rRmZVyAgWgd9VOfoqTkEwSLl5xasgi0kWm4+G4abFGR1F4ivO+aX0d5aLc6g8/krH+S2COydjRF2KyToWVZZpNXYrIDOxVt0CW4Tyh55k3GyrlePPKMKA0WKoklfZh7jWYwkYYix4c/CjMvpEA=:fI0KfucP5l7cl5S+11F0HubnNJi8hSNbWALShpW3Lcw=',
    }

    data = {
        'LatitudeMax': '45.53758',
        'LongitudeMax': '-75.24660',
        'LatitudeMin': '44.96273',
        'LongitudeMin': '-76.35392',
        'Sort': '6-D',
        'PropertyTypeGroupID': '1',
        'PropertySearchTypeId': '1',
        'TransactionTypeId': '2',
        'Currency': 'CAD',
        'RecordsPerPage': '12',
        'ApplicationId': '1',
        'CultureId': '1',
        'Version': '7.0',
        'CurrentPage': str(i)
    }

    # response
    response = requests.post(
        'https://api2.realtor.ca/Listing.svc/PropertySearch_Post', headers=headers, data=data)

    # json object
    response_json = response.json()

    # starting point
    result_items = response_json['Results']

    for result in result_items:

        # address
        try:
            address.append(result['Property']['Address']['AddressText'])
        except:
            address.append('')

        # bedrooms
        try:
            bedrooms.append(result['Building']['Bedrooms'])
        except:
            bedrooms.append('')

        # bathrooms
        try:
            bathrooms.append(result['Building']['BathroomTotal'])
        except:
            bathrooms.append('')

        # agent name
        try:
            agent_name.append(result['Individual'][0]['Name'])
        except:
            agent_name.append('')

        # area code
        try:
            area_code.append(result['Individual'][0]['Phones'][0]['AreaCode'])
        except:
            area_code.append('')

        # phone number
        try:
            phone_number.append(result['Individual']
                                [0]['Phones'][0]['PhoneNumber'])
        except:
            phone_number.append('')

        # price
        try:
            price.append(result['Property']['Price'])
        except:
            price.append('')

df_realtor = pd.DataFrame({'Address': address, 'Bedrooms': bedrooms, 'Bathrooms': bathrooms,
                          'Agent Name': agent_name, 'Area Code': area_code, 'Phone Number': phone_number, 'Price': price})

df_realtor.to_excel('realtor.xlsx', index=False)

engine = sqlalchemy.create_engine(
    'postgresql://postgres:Elgoldony2000..@localhost:5434')
df_realtor.to_sql('realtor_table', engine)
