from alpaca_client.alpaca_serving.client import *
from alpaca_server.alpaca_model.pytorchAPI import *
import alpaca_server.alpaca_model.pytorchAPI.utils as utils

x_train, y_train = utils.load_data_and_labels('train.bio')
sent = x_train[0:10]
label = y_train[0:10]
ac = AlpacaClient()
ac.initiate(1)
ac.online_initiate(x_train[:50], [['B-PER', 'I-PER', 'B-LOC', 'I-LOC', 'B-ORG', 'I-ORG', 'B-MISC', 'I-MISC', 'O']])
ac.online_learning(x_train[:50],y_train[:50])
ac.predict("Paris and New York and Los Angeles")
ac.online_learning(sent,label)
ac.predict("English lamb")
ac.online_learning(sent,label)
ac.active_learning(x_train[:50],2)