TCPClient myTCP;

const char * water_webpage = "agua-flex.herokuapp.com";
const char * url = "/log/";

void sendGetRequest(const char * server, const char * url, int val)
{
    if (myTCP.connect(server, 80)) {
        myTCP.print("GET ");
        myTCP.print(url);
        myTCP.print(val);
        myTCP.println(" HTTP/1.0");
        myTCP.println("Connection: close");
        myTCP.print("Host: ");
        myTCP.println(server);
        myTCP.println("Accept: text/html, text/plain");
        myTCP.println();
        myTCP.flush();
    } 
}

void setup() {
  pinMode(A0, INPUT);
}

void loop() {
    sendGetRequest(water_webpage, url, analogRead(A0));
    delay(20000);
}
