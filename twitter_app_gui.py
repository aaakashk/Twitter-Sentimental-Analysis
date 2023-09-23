import using_twitter_api as t
import ttkbootstrap as ttk

class GUI():

    def __init__(self):
        self.root = ttk.Window()
        self.root.geometry("450x350")
        self.root.resizable(False, False)
        self.root.title('Twitter Sentiment Analysis App')

        self.api = t.authenticate()

        self.frame = ttk.Frame(self.root, bootstyle= "light", width= 400, height= 400)
        self.frame.pack(fill="both", expand= True, padx= 0, pady= 0)

        self.search_label = ttk.Label(self.frame, text= "Search Query:")
        self.search_label.grid(row= 0, column= 0, padx= 50, pady= 10)

        self.entry = ttk.Entry(self.frame, text= "search", bootstyle= "dark")
        self.entry.grid(row= 0, column= 1, padx= 10, pady= 10)

        self.limit_label = ttk.Label(self.frame, text= "Limit:")
        self.limit_label.grid(row= 1, column= 0, padx= 60, pady= 10)

        self.limit = ttk.Entry(self.frame, text= "limit", bootstyle= "dark")
        self.limit.grid(row= 1, column= 1, padx= 10, pady= 10)

        self.search_term = ""
        self.tweet_limit = 0
        self.search_button = ttk.Button(self.frame, text= "Search", command= self.get_result)
        self.search_button.grid(columnspan= 2, padx= 0, pady= 0)

        self.numbers = []

        self.pie_chart_button = ttk.Button(self.frame, text= "Show Pie Chart", command= self.pie_chart, bootstyle= "success")
        self.pie_chart_button.grid(row= 3, column= 0, padx= 10, pady= 10)

        self.bar_chart_button = ttk.Button(self.frame, text= "Show Bar Chart", command= self.bar_chart, bootstyle= "success")
        self.bar_chart_button.grid(row= 3, column= 1, padx= 10, pady= 10)

        self.root.mainloop()

    def get_result(self):
        self.search_term = self.entry.get()
        self.tweet_limit = int(self.limit.get())
        print(self.search_term)
        print(self.tweet_limit)
        tweets = t.get_tweets(self.api, self.search_term, self.tweet_limit)
        self.numbers = t.result(tweets)
    
    def pie_chart(self):
        t.pie_chart(self.numbers)

    def bar_chart(self):
        t.bar_chart(self.numbers)

if __name__ == '__main__':
    GUI()