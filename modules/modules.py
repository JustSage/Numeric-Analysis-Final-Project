import matplotlib.pyplot as plt
import numpy as np
import axes,TableIt,inspect,sympy
from functools import lru_cache
# %%
def strip_lambda(content):
    """
    strip lambda boilderplate from function.
    """
    if content.__name__ == "<lambda>":
        content = str(inspect.getsourcelines(content)[0])
        content = content.strip("['\\n]").split(':')[1] # getting the function as string
        content = content.replace("np.","").replace("sympy.","").replace("math.","")
    return content

class Table (object):
    """
    Table acts as an API for TableIt custom module.
    will be used to create visual tables for our output.
    """
    def __init__(self,table):
        """
        :param: table - expecting a list, initializing a double demansion table.
        """
        self.table = [table]

    def append_row(self,row,prec=1):
        """
        :param: row - the values to add to our table.
        :param: prec - precision given by user.
        """
        self.table.append(row)

    def show_table(self,color=(108,160,220)):
        """
        prints table.
        :param: color - adding color to the first line and row.
        """
        TableIt.printTable(self.table,useFieldNames=True,color=color)

class CartesianPlot (object):
    """
    CartesianPlot acts as an API for matplotlib pyplot custom functions.
    will be used to create a visual graph for our solutions.
    """
    def __init__(self,title):
        """
        Initializes a CartesianPlot.
        :param: title - title to add for the graph.
        """
        # creates a cartesian coordinate system.
        self.x = np.linspace(-10, 10, 1000)
        self.cartesian_coordinate_system = axes.Axes(xlim=(-10, 10),
                ylim=(-10 ,10),
                figsize=(15,15))

        # initializing root arrays (for points on graph)
        self.xs = np.array([])
        self.ys = np.zeros(len(self.xs))

        # will contain all labels in table of context
        self.contents = []
        self.roots = []
        self.count = 0
        # draw cartesian grid
        self.cartesian_coordinate_system.draw()

        plt.suptitle(title)

        # add grid to plot
        plt.grid(True)

    def add_plot_function(self,func,roots,label):
        """
        add a function to the plot.
        :param: func - the function to add.
        :param: roots - a list of roots calculated.
        :param: label - given label to the function.
        """
        # adding the function graph.
        plt.plot(self.x,func(self.x))
        # updating root list
        self.roots = roots
        self.xs = np.append(self.xs,roots)
        self.ys = np.append(self.ys,np.zeros(len(roots)))
        self.count += 1
        
        # stripping lambda content from func
        content = strip_lambda(func)
        # labeling the function
        self.contents.append(label + content)
        self.update_function_legend()
    
    def update_function_legend(self):
        """
        updates the function table of contents using the contents variable.
        """
        # plt.legend(self.contents,loc="lower right",title="Functions:")
        func_legend = plt.legend(self.contents,loc="lower right",title="Functions:")
        plt.gca().add_artist(func_legend)
    
    def draw_roots(self):
        """
        adding roots plot.
        displays a small table of content for the root symbol on the graph.
        it will also annotate the root's around the location of it on the graph.
        """
        for n in range(0,self.count-1):
            plt.plot(self.xs[n],self.ys[n],marker='o',label="Roots") # draw roots
        root_legend = plt.legend(self.contents,loc='lower left',title="Roots")
        plt.gca().add_artist(root_legend)

        # annotate labels to roots
        for x,y in zip(self.xs,self.ys):
            label = "{:.2f}".format(x)
            plt.annotate(label, # this is the text
                        (x,y), # this is the point to label
                        textcoords='offset pixels', # how to position the text
                        xytext=(0,3), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center

    def plot_savefig(self,filepath):
        """
        saving figure to path.
        :param: filepath - the path i wish to save the graph in.
        """
        plt.savefig(filepath, bbox_inches='tight')
            

# Usage Example
func1 = lambda x: x
func2 = lambda x: x**4 - x - 1
func3 = lambda x: x**2 - x - 1
func4 = lambda x: x**5 - x - 1
func5 = lambda x: np.sin(x)
func6 = lambda x: x**3 - x - 1
func7 = lambda x: x**4 - x - 1
func8 = lambda x: x**2 - x - 1
func9 = lambda x: x**5 - x - 1
func10 = lambda x: np.cos(x) + 1

cp = CartesianPlot("Testing Graph")
cp.add_plot_function(func1,[1],"f1=")
cp.add_plot_function(func2,[2],"f2=")
cp.add_plot_function(func3,[3],"f3=")
cp.add_plot_function(func4,[4],"f4=")
cp.add_plot_function(func9,[9],"f9=")
cp.add_plot_function(func10,[10],"f10=")
cp.draw_roots()
# cp.update_function_legend()
# cp.draw_roots()
# cp.plot_savefig('./images/graph_1')

cp2 = CartesianPlot("Testing 2")
cp2.add_plot_function(func5,[5],"f5=")
cp2.add_plot_function(func6,[6],"f6=")
cp2.add_plot_function(func7,[7],"f7=")
cp2.add_plot_function(func8,[8],"f8=")



# cp2.update_function_legend()
# cp2.draw_roots()
# cp2.plot_savefig('./images/graph_2')
# %%


t = Table(['a','b','c','d','e','f','g'])
t.append_row([3,3,3,3,3,3,3])
t.append_row([3,2,5,3,3,2,3])
t.append_row([4,1,1,4,4,2,3])
t.show_table()