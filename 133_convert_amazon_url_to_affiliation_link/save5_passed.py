def generate_affiliation_link(url):
    part1 = "".join(url.split('/')[:3])
    part2 = "".join(url.rsplit('/')[5])
    return f"{part1}/dp/{part2}/?tag=pyb0f-20".replace(part1, "http://www.amazon.com")