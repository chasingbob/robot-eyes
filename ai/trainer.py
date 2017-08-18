'''
Deep Learning wrapper trainer class

'''


class Trainer:
    '''
    Deep Learning Trainer Class
    '''

    def build(self):
        '''
        Compile the Training model 
        '''
        pass
    
    def train(self):
        '''
        Train the model
        '''
        pass
    
    def save(self, top_layers_only=False):
        '''
        Save the model
        '''
        pass

    def load(self, file_name):
        '''
        Load model from file
        '''
        pass
    
    def predict(self, img):
        '''
        Make a prediction against model
        '''
        pass


