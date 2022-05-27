def outlier_bounds(seq, scale):
    q1, q3 = seq.quantile(0.25), seq.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - scale*iqr
    upper_bound = q3 + scale*iqr
    return (lower_bound, upper_bound)

def remove_groupby_outliers(df, by, col, scale):
    outlier_idx = []

    for _, group in df.groupby(by):
        group_lower, group_upper = outlier_bounds(group[col], scale)
        group_outlier_idx = group[(group[col] < group_lower) | (group[col] > group_upper)].index
        outlier_idx.extend(group_outlier_idx)

    df_without_outliers = df.drop(outlier_idx)
    return df_without_outliers