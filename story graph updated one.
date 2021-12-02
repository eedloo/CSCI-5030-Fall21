from inputActions import Input_Actions
import menu
from showoptions import ShowOptions
class ExecuteStory:
    def _init_(self, graph_inputs):
        self.graph_inputs = graph_inputs

    def execute(self):
       if 'EnableInput' in self.graph_inputs.options:
          position = self.graph_inputs.options.index('EnableInput')
          first_part = self.graph_inputs.options[:position]
          input_acts = Input_Actions(first_part)
          menu.show_menu()
          opt1 = self.graph_inputs.options[position+1]
          opt2 = self.graph_inputs.options[postion+2]
          show_opt = ShowOptions(opt1, opt2)
          show_opt.show_options()
          selected_option = show_opt.get_selected_option()
          show_opt.disable_icon(selected_option)
          second_option = self.graph_inputs.options[position+1]
          input_acts = Input_Actions(second_option)
          menu.show_menu()
       else :
         input_acts = Input_Actions(self.graph_inputs.options)
         menu.show_menu()
       if self.graph_inputs.left != None:
         if self.graph_inputs.right != None:
           while (True):
             input()
         else:
            self.graph_inputs = self.graph_inputs.right
            execute()
       else:
         self.graph_inputs = self.graph_inputs.left
         execute()

ex = ExecuteStory(graph)
ex.execute()
