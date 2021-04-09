from alpaca_client.alpaca_serving.client import *
from alpaca_server.alpaca_model.pytorchAPI import *
from alpaca_server.alpaca_model.pytorchAPI import utils
x_train, y_train = utils.load_data_and_labels('china.bio')
print("load ok ")
sent = x_train[0:10]
label = y_train[0:10]
ac = AlpacaClient(timeout=100000)
ac.initiate(6)
ac.online_initiate(x_train, [['B_LOC', 'B_ORG', 'B_PER', 'B_T','I_LOC','I_ORG','I_PER', 'I_T','O']])
ac.online_learning(x_train[:1000],y_train[:1000],1,100)
ac.predict("3月3日")
