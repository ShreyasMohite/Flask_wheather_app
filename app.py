

from flask import Flask,render_template,url_for,redirect,session,request
import requests

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def home():
    try:
        name = request.form.get("just")
        if name:
            url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=43ee602cd3f013c1a0c2fa793155236e'.format(name)
        else:
            url='https://api.openweathermap.org/data/2.5/weather?q=mumbai&appid=43ee602cd3f013c1a0c2fa793155236e'
        whether=requests.get(url).json()
        wl=[]
        whe={
        'description':whether['weather'][0]['description'],
        'name':whether['name'],
        'temp':whether['main']['temp'],
        'humidity':whether['main']['humidity'],
        'speed':whether['wind']['speed'],
        'country':whether['sys']['country']
        }
        wl.append(whe)
    except Exception as e:
        print(e)

    return render_template("home.html",title="home",name=wl)
   


if __name__ == "__main__":
    app.run(debug=True)