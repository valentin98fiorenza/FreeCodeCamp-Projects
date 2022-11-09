import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col=['date'])

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(df.index, df['value'], color='r')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_bar = df_bar.groupby(['year', 'month'])        ['value'].mean()
    df_bar = df_bar.unstack()

    # Draw bar plot

    fig = df_bar.plot.bar(legend=True, figsize=(10,10),      xlabel='Years', ylabel='Average Page Views').figure
    plt.legend(['January', 'February', 'March', 'April',     'May', 'June', 'July', 'August', 'September',            'October', 'November', 'December'], title='Months')



    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month'] = pd.Categorical(df_box['month'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    df_box = df_box.sort_values(by='month')
    fig, axs = plt.subplots(1, 2, figsize=(14, 4))
    sns.boxplot(ax=axs[0], x = 'year', y = 'value', data = df_box).set(title = "Year-wise Box Plot (Trend)", xlabel='Year', ylabel='Page Views')
    sns.boxplot(ax=axs[1], x = 'month', y = 'value', data = df_box).set(title = "Month-wise Box Plot (Seasonality)", xlabel='Month', ylabel='Page Views')
    axs[0].set_yticks([0,20000,40000,60000,80000,100000,120000,140000,160000,180000,200000])
    axs[1].set_yticks([0,20000,40000,60000,80000,100000,120000,140000,160000,180000,200000]);




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
