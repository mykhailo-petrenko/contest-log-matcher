import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context


def clear_row(row):
    return row.replace('\\n', '').replace('\\t', '').strip()


def load_member_list(url):
    http = urllib.request.urlopen(url)
    raw = http.read().decode('utf-8')
    members_raw = raw.strip().split('|')

    members = []

    for member_raw in members_raw:
        member_raw = clear_row(member_raw)

        if not member_raw:
            continue

        properties = member_raw.split(',')
        properties = [property.strip() for property in properties]

        members.append(tuple(properties[1:]))

    return members



def main():
    url = "https://pi4ntc.nl/wp-admin/admin-ajax.php?action=memberlist"
    members = load_member_list(url)
    print("\n".join([",".join(m) for m in members]))


if __name__ == "__main__":
    main()
