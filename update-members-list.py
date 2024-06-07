import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

# https://pi4ntc.nl/wp-admin/admin-ajax.php?action=memberlist


def clear_row(row):
    return row.replace('\\n', '').replace('\\t', '').strip()


def load_member_list(url):
    http = urllib.request.urlopen(url)
    raw = str(http.read())
    members_raw = raw.split('|')
    print("----")
    for member_raw in members_raw:
        member_raw = clear_row(member_raw)
        properties = member_raw.split('\n')
        properties = [property.strip() for property in properties]
        print(properties)

def main():
    url = "https://pi4ntc.nl/wp-admin/admin-ajax.php?action=memberlist"
    load_member_list(url)


if __name__ == "__main__":
    main()
