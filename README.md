# A Natural Language Processing Framework for Training a Neural Network Chatbot

<h2 align="center">About Project</h2>
### Project Explanation
The general context behind our project was to develop chatbot which could be trained on a given data set. Our first approach was to use **Google AIY Kit** and modify it to our needs, however while setting it up and experimenting with it we found out we could not achieve that. There were predefined programs ready for our use, which would mean it would not require much coding from us. Another issue with that approach were the dependencies and documentation that were not reliable.

With that in mind we have decided that the best option for us would be to start from the beginning and develop our own chatbot from scratch. The chatbot we came up with, is using **tensorflow** to train data on a given model classification and then build upon that to handle responses once given input from the user. Further we added **client-server** side so that all the necessary response data could be stored on the **server** side, while **client** took care of interaction between user and the chatbot through the use of GUI (Graphical User Interface) which was coded up using **TkInter**.

Simply put the way our project works is as follows:
* Data extraction:
  * This mainly happens in 'get_data.py' where depending on input it generates a set of exchanges of conversations between two people on a given topic from corpus data.
* Data conversion:
  * This happens in **txtToCsv.py** and **csvToJson.py**
  * **txtToCsv.py** loops through all the conversations stored in dialogues folder and converts them all into CSV(Comma-Separated Values) format, also called excel format, into a single CSV file.
  * **csvToJson.py** converts previously generated CSV file into a JSON(JavaScript Object Notation) format. Main reason for this is that training was set up in a way to accept only JSON file formats.
* Clean up:
  * After successful extraction and conversion of data, next step is to check if the file is correctly set up after which data then can be added to the main data collection which is stored inside **intents.json** file.
* Training:
  * Training happens in **chat_model.py** using **intents.json** file.
* Response Handler:
  * Response hadnler is responsible to handle responses between user and the chatbot and it's happening in **chat_response.py**.
* Server:
  * On server side is where data, training data, and response handler is stored.
  * Server allows up to five connections at the same time, and **server.py** file is responsible for those actions.
  * Server is connected up with response handler, as it handles user requests.
* Client:
  * Client is responsible for interaction between user and the chatbot. It is where data is displayed visually through the use of GUI.
  * Client sends requests with a given message over the socket connection, and it receives back a response from a server which is then displayed in the GUI.
  * Logic behind the client and it's GUI can be seen in **client.py** file.
  
### Project Structure
### Required to Run
### How to Run
### Example Output

<h2 align="center">Background on Technologies Researched</h2>

### Artificial Intelligence
### Natural Language Processing
### TensorFlow
### Neural Networks

<h2 align="center">References</h2>
