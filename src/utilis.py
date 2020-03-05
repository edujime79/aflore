import sqlite3
import pandas as pd
import src.config as cfg


def get_db_connector():
    """ Return a sql connector to the db

    Returns
    -------
    connector a sqlite3.connect
    """

    con = sqlite3.connect(cfg.db_file_path)

    return con


def run_query(query):
    """Run a query and return results as a pandas dataframe

    Parameters
    ----------
        query (str): query to run

    Returns
    -------
        Dataframe
    """

    conn = get_db_connector()

    data = pd.read_sql(query, conn)
    conn.close()
    return data


def get_var_distibution(data, variable):
    """
        Parameters
    ----------
        data (dataframe): a dataframe that contain var
        variable (str): a variable name

    Returns
    -------
        Dataframe with hist
    """
    counts = data[variable].value_counts(dropna=False)
    counts = counts.to_frame(name="count")
    counts["percentage"] = counts["count"]/sum(counts["count"])
    counts[variable] = counts.index
    out = counts[[variable, "count", "percentage"]].reset_index(drop=True)

    return out


def get_var_groupby_avg(data, group, variable):
    """
        Parameters
    ----------
        data (dataframe): a dataframe that contain var
        group (str): variable name to group information
        variable (str): a variable name

    Returns
    -------
        Dataframe with hist
    """

    avgs = data.groupby(group)[variable].mean()
    count = data.groupby(group)[variable].count()
    avgs = avgs.to_frame(name="average")
    avgs["count"] = count
    avgs[group] = avgs.index
    avgs = avgs[[group, "average", "count"]].reset_index(drop=True)

    return avgs


def export_results(data, response):
    """
            Parameters
    ----------
        data (dataframe): a dataframe to export
        response(str): response count

    """

    out_file = "{0}//{1}.xlsx".format(cfg.folder_assets_out, response)
    return data.to_excel(out_file, index=False)

