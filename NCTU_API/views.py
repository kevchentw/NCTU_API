from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny


@api_view(('GET',))
@permission_classes((AllowAny,))
def nctu_api_root(request, format=None):
    """
#NCTU OPEN API
We are now under development...<br>
If you are interested, please join our <a href="https://www.facebook.com/groups/331427716981279/"> Facebook Group</a><br>
##Test Account
Username: ``test``<br>
Password: ``test``<br>
##Token
You can get the access token from by
``POST https://api.nctu.me/api-token-auth/``<br>
##Example:<br>
###Curl <br>
<pre class="prettyprint"><code class="language-sh">\#Get Token:
curl --data "username=test&password=test"  https://api.nctu.me/api-token-auth/
\#Start Using API
curl -X GET https://api.nctu.me/ -H 'Authorization: Token 290af1f32c268c9765c558d0d4a9cdd17d62f4d2'
</code></pre>
###Python (With Requests Library)
<pre class="prettyprint"><code class="language-py">import requests
import json
\# Get Token
token_url = "https://api.nctu.me/api-token-auth/"
payload = {'username': 'test', 'password': 'test'}
r_token = requests.post(token_url, data=payload, verify=True)
token = json.loads(r_token.text)['token']
\# Using API
api_url = "https://api.nctu.me/"
headers = {'Authorization': 'Token %s' % token}
r_api = requests.post(api_url, headers=headers, verify=True)
result = json.loads(r_api.text)
</code></pre>
### Ajax <br>
<pre class="prettyprint"><code class="language-js">function getToken(){
    $.ajax({
        url : "https://api.nctu.me/api-token-auth/",
        type: "POST",
        data : {'username': 'test', 'password': 'test'},
        success: function(data){
            return data['token'];
        },
    });
}
$.ajax({
    url : "https://api.nctu.me/",
    beforeSend : function(xhr) {
      xhr.setRequestHeader("Authorization", "Token " + getToken());
    },
    type: "GET",
    success: function(data)
    {
        console.log(data);
    },
});
</code></pre>
#API List
    """
    return Response(
            {
                'bus': reverse('bus', request=request, format=format),
                'mail': reverse('mail-list', request=request, format=format),
                'building': reverse('building', request=request, format=format)
                })


