def main():
    test_data = [
        [
            "3",
            "France 1 4 4 6",
            "Spain 3 1 6 3",
            "Portugal 1 1 2 2"
        ],
        [
            "1",
            "Luxembourg 1 1 1 1"
        ],
        [
            "2",
            "Netherlands 1 3 2 4",
            "Belgium 1 1 2 2"
        ]
    ]

    case_num = 1
    for data in test_data:
        c = int(data[0])
        countries = []
        for i in range(1, c + 1):
            parts = data[i].split()
            name = parts[0]
            xl, yl, xh, yh = map(int, parts[1:])
            countries.append((name, xl, yl, xh, yh))

        max_x = max(xh for _, xl, _, xh, _ in countries)   # 
        max_y = max(yh for _, _, yl, _, yh in countries)

        grid = [[None] * (max_y + 1) for _ in range(max_x + 1)]
        for idx, (_, xl, yl, xh, yh) in enumerate(countries):
            for x in range(xl, xh + 1):
                for y in range(yl, yh + 1):
                    grid[x][y] = idx

        motifs = len(countries)
        currents = [[[0] * motifs for _ in range(max_y + 1)] for _ in range(max_x + 1)]
        for idx, (_, xl, yl, xh, yh) in enumerate(countries):
            for x in range(xl, xh + 1):
                for y in range(yl, yh + 1):
                    currents[x][y][idx] = 1000000.0  # 

        done = [None] * motifs
        days = 0
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check_country(index):  # 
            _, xl, yl, xh, yh = countries[idx]
            for x in range(xl, xh + 1):
                for y in range(yl, yh + 1):
                    if any(currents[x][y][m] == 0 for m in range(motifs)):
                        return False
            return True

        while True:
            for idx in range(motifs):
                if done[idx] is None and check_country(idx):
                    done[idx] = days

            if all(d is not None for d in done):
                break

            send = [[[0] * motifs for _ in range(max_y + 1)] for _ in range(max_x + 1)]
            for x in range(1, max_x + 1):
                for y in range(1, max_y + 1):
                    if grid[x][y] is None:
                        continue
                    for m in range(motifs):
                        rep = currents[x][y][m] / 1000  # 
                        if rep > 0:
                            count_neighbors = 0
                            for dx, dy in neighbors:
                                nx, ny = x + dx, y + dy
                                if 1 <= nx <= max_x and 1 <= ny <= max_y and grid[nx][ny] is not None:
                                    send[nx][ny][m] += int(rep)
                                    count_neighbors += 1
                            send[x][y][m] -= int(rep) * count_neighbors

            for x in range(1, max_x + 1):
                for y in range(1, max_y + 1):
                    if grid[x][y] is None:
                        continue
                    for m in range(motifs):
                        currents[x][y][m] += send[x][y][m]

            days =+ 1  #

        result = [(countries[i][0], done[i]) for i in range(motifs)]
        result.sort(key=lambda x: (x[1], x[0]))

        print(f"Case Number {case_num}")
        for name, d in result:
            print(f"{name} {d}")
        case_num += 1


if __name__ == "__main__":
    main()
