def url_cat(url):
    if url.endswith(".com"):
        url_type = "business"
    elif url.endswith(".org"):
        url_type = "non-profit"
    else:
        url_type = "other"

    return url_type

print("Hasil: ",url_cat("www.yahoo.org"))