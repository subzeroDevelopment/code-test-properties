import requests

BASE_URL = "https://api.mocklets.com/p68140/properties"


def get_properties():
  req = requests.get(BASE_URL)
  if req.status_code!=200:
    return []
  return req.json()

def get_property_by_name(name:str):
  properties = get_properties()
  prop = list(filter(lambda a: a['name']==name,properties))
  return None if len(prop)<1 else prop[0]

def get_property_by_type(types:list):
  properties = get_properties()
  return list(filter(lambda a:a['type'] in types,properties))

def get_property_by_facilities(facilities:list):
  properties = get_properties()
  tmp_prop = []
  for fac in facilities:
    tmp_prop.extend(
      list(
        filter(lambda a:fac in a['facilites'],properties)
      )
    )
  return tmp_prop

def get_properties_report():
  properties = get_properties()
  t_types = []
  for prop in properties:
    if prop['type']not in t_types:
      t_types.append(prop['type'])

  sum_by_type = list(
    map(lambda a:
      (a,len(list(filter(lambda b:b!=None,
            [prop if prop['type']==a else None for prop in properties]
          )
        )
        )
      ),
      t_types
    )
  )
  tmp_facilities = []
  for prop in  properties:
    for fac in prop['facilites']:
      if fac not in tmp_facilities:
        tmp_facilities.append(fac)
  
  sum_by_fac = list(
    map(lambda a:
      (a,len(list(filter(lambda b:b!=None,
            [prop if a in prop['facilites'] else None for prop in properties]
          )
        )
        )
      ),
      tmp_facilities
    )
  )


  return {
    "num_of_properties": len(properties),
    "num_of_properties_by_type": sum_by_type,
    "num_of_properties_by_facilities": sum_by_fac
  }


print(get_properties_report())
    
  


