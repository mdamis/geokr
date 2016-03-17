import requests
import json
import io

'''
This class allow sending http request on Flickr API. The Json result is automaticcally parsed.
'''
class Flickr:
    request_baseurl = 'https://api.flickr.com/services/rest/'
    jsonDecoder = json.JSONDecoder()
    
    '''
    Flickr constructor
    
    @param stirng api_key - Your Flickr API key
    '''
    def __init__(self, api_key):
        
        
        self.api_key = api_key

    def request(self, method, args):
        url = self.request_baseurl + '?api_key=' + self.api_key + '&format=json&method=' + method + '&' + '&'.join([k+'='+str(v) for k,v in args.iteritems()])
        return self.jsonDecoder.decode(requests.get(url).content[len("jsonFlickrApi("):-1])
    
    def doRequest(self, offset, nb_page, method, args):
        data=[]
        for page in range(nb_page):
            args['page'] = offset + page + 1
            print "fetching page number %d/%d (%d photos) " % ((page+1), nb_page, len(data))
            data += flickr.request(method, args)["photos"]["photo"]
            
        print "fetching end Total : %s photos requested" % (len (data))
        return data

    def saveData(self, data, save_file):
        with io.open(save_file, 'w', encoding='utf-8') as f:
            f.write(unicode(json.dumps(data,indent=4, ensure_ascii=False)))
        print '%s lines of data saved to %s' %(len(data), save_file)
        
    def loadDataFromFile(self, load_file):
        with open(load_file) as photos_json:
            return json.load(photos_json)