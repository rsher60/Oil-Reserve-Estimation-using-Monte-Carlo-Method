from PyQt4 import QtCore, QtGui
from OIL2 import Ui_MainWindow



import sys
import statistics as statistics
import scipy as sp
import numpy as np
from scipy import stats
import matplotlib as mpl
from matplotlib import pyplot as plt
from bisect import bisect_left
from scipy.interpolate import UnivariateSpline

class discrete_cdf:
     def __init__(data):
          self._data = data # must be sorted
          self._data_len = float(len(data))

     def __call__(point):
          return (len(self._data[:bisect_left(self._data, point)]) / 
                  self._data_len)


class simulator(QtGui.QMainWindow,Ui_MainWindow):

     def __init__(self,parent=None):

         QtGui.QMainWindow.__init__(self,parent)
         self.setupUi(self)

         self.comboBox.activated.connect(self.select) 
         self.comboBox_2.activated.connect(self.select)
         self.comboBox_3.activated.connect(self.select)
         self.comboBox_4.activated.connect(self.select)
         self.comboBox_5.activated.connect(self.select)

         self.pushButton.clicked.connect(self.est) 


     def select(self):
         
                 if self.comboBox.currentText()=="TRIANGULAR":
                    self.label_6.setText("MAXIMUM")
                    self.label.setText("MINIMUM")
                    self.label_16.show()
                    self.lineEdit_11.show()
                 else:
                    self.label_6.setText("MEAN")
                    self.label.setText("ST DEVIATION")
                    self.label_16.hide()
                    self.lineEdit_11.hide()

                 if self.comboBox_2.currentText()=="TRIANGULAR":
                    self.label_7.setText("MAXIMUM")
                    self.label_2.setText("MINIMUM")
                    self.label_17.show()
                    self.lineEdit_12.show()
                 else:
                    self.label_7.setText("MEAN")
                    self.label_2.setText("ST DEVIATION")
                    self.label_17.hide()
                    self.lineEdit_12.hide()

                 if self.comboBox_3.currentText()=="TRIANGULAR":
                    self.label_8.setText("MAXIMUM")
                    self.label_3.setText("MINIMUM")
                    self.label_18.show()
                    self.lineEdit_13.show()
                 else:
                    self.label_8.setText("MEAN")
                    self.label_3.setText("ST DEVIATION")
                    self.label_18.hide()
                    self.lineEdit_13.hide()

                 if self.comboBox_4.currentText()=="TRIANGULAR":
                    self.label_9.setText("MAXIMUM")
                    self.label_4.setText("MINIMUM")
                    self.label_19.show()
                    self.lineEdit_14.show()
                 else:
                    self.label_9.setText("MEAN")
                    self.label_4.setText("ST DEVIATION")
                    self.label_19.hide()
                    self.lineEdit_14.hide()

                 if self.comboBox_5.currentText()=="TRIANGULAR":
                    self.label_10.setText("MAXIMUM")
                    self.label_5.setText("MINIMUM")
                    self.label_20.show()
                    self.lineEdit_15.show()
                 else:
                    self.label_10.setText("MEAN")
                    self.label_5.setText("ST DEVIATION")
                    self.label_20.hide()
                    self.lineEdit_15.hide()
          
     def est(self):

          M1=self.lineEdit_6.text()
          S1=self.lineEdit.text()

          M2=self.lineEdit_7.text()
          S2=self.lineEdit_2.text()

          M3=self.lineEdit_8.text()
          S3=self.lineEdit_3.text()

          M4=self.lineEdit_9.text()
          S4=self.lineEdit_4.text()

          M5=self.lineEdit_10.text()
          S5=self.lineEdit_5.text()


          N1=self.lineEdit_11.text()
          N2=self.lineEdit_12.text()
          N3=self.lineEdit_13.text()
          N4=self.lineEdit_14.text()
          N5=self.lineEdit_15.text()


          



          y = 1;
          aOIP = []
          P = []
          P_2= []
          P_3= []
          P_4= []
          P_5= []
          while y <= 1000:

               if self.comboBox.currentText()=="TRIANGULAR":
                    

                  p = np.random.triangular(S1,N1,M1,1)

               elif self.comboBox.currentText()=="LOG NORMAL":

                    p = np.random.lognormal(M1,S1,1)

               else :

                    p = np.random.normal(M1,S1,1)

               



               if self.comboBox_2.currentText()=="TRIANGULAR":
                    

                    p_2= np.random.triangular(S2,N2,M2,1)

               elif self.comboBox_2.currentText()=="LOG NORMAL":

                    p_2= np.random.lognormal(M2,S2,1)

               else :
                    

                    p_2= np.random.normal(M2,S2,1)

               

               if self.comboBox_3.currentText()=="TRIANGULAR":

                    p_3= np.random.triangular(S3,N3,M3,1)

               elif self.comboBox_3.currentText()=="LOG NORMAL":

                    p_3= np.random.lognormal(M3,S3,1)

               else :

                    p_3= np.random.normal(M3,S3,1)

               

               if self.comboBox_4.currentText()=="TRIANGULAR":

                    p_4= np.random.triangular(S4,N4,M4,1)

               elif self.comboBox_4.currentText()=="LOG NORMAL":

                    p_4= np.random.lognormal(M4,S4,1)

               else :

                    p_4= np.random.normal(M4,S4,1)

               

               if self.comboBox_5.currentText()=="TRIANGULAR":

                   p_5= np.random.triangular(S5,N5,M5,1)

               elif self.comboBox_5.currentText()=="LOG NORMAL":

                   p_5= np.random.lognormal(M5,S5,1)

               else :

                   p_5= np.random.normal(M5,S5,1)


               



               OIP = 7758 * (p * p_2 *(1-p_3)* p_4)/(p_5)
               aOIP.append(OIP)
               P.append(p)
               P_2.append(p_2)
               P_3.append(p_3)
               P_4.append(p_4)
               P_5.append(p_5)
               y = y+1;
     


          # CUMULATIVE DISTRIBUTION CURVE  
          X=sorted(aOIP)
          Y=[]
          l=len(X)
          Y.append(float(1)/l)
          for i in range(2,l+1):
                Y.append(float(1)/l+Y[i-2])
          
          fig1 = plt.figure()
          ax1 = fig1.add_subplot(111)
          ax1.plot(X, Y)
          fig1.suptitle('CUMULATIVE RESERVES DISTRIBUTION ', fontsize=20)
          plt.xlabel('RESERVES (STB)', fontsize=18)
          plt.ylabel('CUMULATIVE PROBABILITY DENSITY', fontsize=16)
          plt.draw()
          plt.show()

          # POROSITY  
          m,x =np.histogram(P,bins=10)
          x = x[:-1] +(x[1]+ x[0])/2
          f = UnivariateSpline(x,m)
          fig2 = plt.figure()
          ax2 = fig2.add_subplot(111)
          ax2.plot(x, f(x))
          fig2.suptitle('POROSITY PROBABILITY DISTRIBUTION', fontsize=20)
          plt.xlabel('POROSITY (%)', fontsize=18)
          plt.ylabel('PROBABILITY DENSITY', fontsize=16)
          plt.draw()
          plt.show()
          
          # AREA        
          m,x =np.histogram(P_2,bins=100)
          x = x[:-1] +(x[1]+ x[0])/2
          f = UnivariateSpline(x,m)
          fig3 = plt.figure()
          ax3 = fig3.add_subplot(111)
          ax3.plot(x,f(x))
          fig3.suptitle('AREA PROBABILITY DISTRIBUTION', fontsize=20)
          plt.xlabel('AREA (acres)', fontsize=18)
          plt.ylabel('PROBABILITY DENSITY', fontsize=16)
          plt.draw()
          plt.show()
          
          # WATER SATURATION
          m,x =np.histogram(P_3,bins=100)
          x = x[:-1] +(x[1]+ x[0])/2
          f = UnivariateSpline(x,m)
          fig4 = plt.figure()
          ax4 = fig4.add_subplot(111)
          ax4.plot(x, f(x))
          fig4.suptitle('WATER SAT. PROBABILITY DISTRIBUTION', fontsize=20)
          plt.xlabel('WATER SAT. (Fraction)', fontsize=18)
          plt.ylabel('PROBABILITY DENSITY', fontsize=16)
          plt.draw()
          plt.show()
          
          # PAY THICKNESS
          m,x =np.histogram(P_4,bins=100)
          x = x[:-1] +(x[1]+ x[0])/2
          f = UnivariateSpline(x,m)
          fig5 = plt.figure()
          ax5 = fig5.add_subplot(111)
          ax5.plot(x, f(x))
          fig5.suptitle('PAY THICK. PROBABILITY DISTRIBUTION', fontsize=20)
          plt.xlabel('PAY THICKNESS (Feet)', fontsize=18)
          plt.ylabel('PROBABILITY DENSITY', fontsize=16)
          plt.draw()
          plt.show()

          #FVF
          m,x =np.histogram(P_5,bins=100)
          x = x[:-1] +(x[1]+ x[0])/2
          f = UnivariateSpline(x,m)
          fig6 = plt.figure()
          ax6 = fig6.add_subplot(111)
          ax6.plot(x, f(x))
          fig6.suptitle('OIL FVF PROBABILITY DISTRIBUTION', fontsize=20)
          plt.xlabel('OIL FORMATION VOLUME FACTOR (bbl/STB)', fontsize=18)
          plt.ylabel('PROBABILITY DENSITY', fontsize=16)
          plt.draw()
          plt.show()




          a = input('\n\n Enter the desired probability(%) :    ')
          d = np.percentile(X, a)
          print('The reserves value associated with the probability',a,'is', d/1000000, 'million bbl')
     

if __name__=='__main__':

    app = QtGui.QApplication(sys.argv)
    sim = simulator()
    sim.show()
    sys.exit(app.exec_())
