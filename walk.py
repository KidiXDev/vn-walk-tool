import requests
import re
import sys
import argparse

# This script is used to get the URL of a VN walkthrough from Seiya-Saiga's website.
WALK_ROOT = "http://seiya-saiga.com/game/"


def print_walks(html):
    regex = re.compile(
        r'<td align="left"><B><A href="(?P<url>[^"]+)">(?P<title>[^<]+)</A></B></td>')
    game_urls = {}
    for match in regex.finditer(html):
        title = match.group("title")
        url = match.group("url")
        game_urls[title] = url
    return game_urls


# Save the results to a file
def save_to_file(data):
    with open('output.txt', 'w', encoding='utf-8') as f:
        for title, url in data.items():
            f.write(f"{title} - {WALK_ROOT}{url}\n")


def get_url_by_title(title, save_output=False):
    URL = "http://seiya-saiga.com/game/kouryaku.html"
    response = requests.get(URL)
    response.encoding = 'shift_jis'
    if response.status_code == 200:
        game_urls = print_walks(response.text)
        search_title = title.strip().lower()

        # try exact match
        if title in game_urls:
            result = {title: game_urls[title]}
            if save_output:
                save_to_file(result)
            return f"{WALK_ROOT}{game_urls[title]}"

        # try case-insensitive match
        for game_title, url in game_urls.items():
            if game_title.lower() == search_title:
                full_url = f"{WALK_ROOT}{url}"
                if save_output:
                    save_to_file({game_title: url})
                return full_url
    return None


def get_walk(save_output=False, quiet=False):
    URL = "http://seiya-saiga.com/game/kouryaku.html"
    response = requests.get(URL)
    response.encoding = 'shift_jis'
    if response.status_code == 200:
        game_urls = print_walks(response.text)
        if not quiet:
            for title, url in game_urls.items():
                print(f"{title} - {WALK_ROOT}{url}")

        if save_output:
            save_to_file(game_urls)
            print("Results saved to output.txt")
    else:
        print(f"Failed to retrieve data: {response.status_code}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Seiya-Saiga VN Walkthrough URL Tool',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '-s', '--search',
        help='Search for a specific vn title\nExample: walk.py -s "VN Title" (the title should be in japanese)')
    parser.add_argument(
        '-o', '--output',
        action='store_true',
        help='Save results to output.txt\nCan be used alone or with -s')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if args.search:
        url = get_url_by_title(args.search, args.output)
        if url:
            print(f"Found URL: {url}")
        else:
            print(f"No URL found for title: {args.search}")
    elif args.output:
        get_walk(True, quiet=True)
    else:
        parser.print_help()
