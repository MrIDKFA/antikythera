import sys
sys.path.append('./src_py')
from rambo_lib import it_data_copy, terminy_data_copy


def main():
    it_data_copy()
    terminy_data_copy()






   
    # Store your data in CSV files. Make sure the data is organized in a way that makes it easy to process and analyze.

    # Import the data from the CSV files into your program. You can use the pandas library in Python to do this. Pandas is a powerful and flexible library that provides data structures for efficiently storing large datasets and tools for working with them.

    # Preprocess the data to prepare it for analysis. You may need to clean the data, handle missing values, or transform the data in some other way to make it suitable for analysis.

    # Analyze the data to generate insights and statistics. You can use pandas and other Python libraries, such as numpy and matplotlib, to calculate and visualize various statistics, such as means, medians, and standard deviations, and to create charts and graphs.

    # Create a dashboard to present the results of your analysis. There are several libraries in Python that can help you with this, such as dash or plotly. These libraries make it easy to create interactive, web-based dashboards that display data in a clear and visual way.

    # Deploy your system online. You can use platforms like Heroku or AWS to host your system, or you can use a dedicated server.

if __name__ == "__main__":
    main()
