public class theater {
    //착각주의! 변수 이름만 정해두었다. 아직 뭘 만든게 아니다!
    private seat[][] seats;
    private int rowCount, colCount;

    public theater(int rowCount, int colCount) {
        //실제 배열을 만들어서 변수에 지정하고
        this.seats = new seat[rowCount][colCount];

        //자리를 전부 Seat로 채우고
        for (int i = 0; i <= rowCount - 1; i++) {
            for (int j = 0; j <= colCount - 1; j++) {
                this.seats[i][j] = new seat();
            }
        }

        //파라미터는 변수에 지정
        this.rowCount = rowCount;
        this.colCount = colCount;
    }

    public void printSeatMatrix() {
        System.out.print("  ");
        for (int i = 1; i <= 9; i++) {
            System.out.print("  " + i);
        }
        System.out.println();

        for (int i = 0; i < rowCount; i++) {
            System.out.print((char) ('A' + i) + ": ");
            for (int j = 0; j < colCount; j++) {
                seat s = seats[i][j];
                if (s.isOccupied()) {
                    System.out.print("[O]");
                } else {
                    System.out.print("[ ]");
                }
            }
            System.out.println();
        }
    }

    public boolean reserve(String name, char rowChar, int col, int numSeat) {
        if (0 <= getRowIndex(rowChar) && getRowIndex(rowChar)<= this.rowCount - 1) {
            if (0 <= col - 1 && col + numSeat - 2 <= this.colCount - 1) {
                for (int i = col - 1; i <= col + numSeat - 2; i++) {
                    if (seats[getRowIndex(rowChar)][i].isOccupied() == false) {
                        continue;
                    } else {
                        return false;
                    }
                }
                for (int i = col - 1; i <= col + numSeat - 2; i++) {
                    seats[getRowIndex(rowChar)][i].reserve(name);
                }
                return true;
            } else {
                return false;
            }
        }
        return false;
    }

    public int cancel(String name) {
        int canceled = 0;
        for (int i = 0; i <= this.rowCount - 1; i++) {
            for (int j = 0; j <= this.colCount - 1; j++) {
                if (this.seats[i][j].match(name) == true) {
                    this.seats[i][j].cancel();
                    canceled++;
                }
            }
        }
        return canceled;
    }

    public int cancel(char rowChar, int col, int numSeat) {
        int canceled = 0;
        for (int i = col - 1; i <= col + numSeat - 2; i++) {
            if (this.seats[getRowIndex(rowChar)][i].isOccupied() == true) {
                this.seats[getRowIndex(rowChar)][i].cancel();
                canceled++;
            }
        }
        return canceled;
    }

    private int getRowIndex(char uppercaseChar) {
        return uppercaseChar - 'A';
    }

    public int getNumberOfReservedSeat() {
        int num = 0;
        for (int i = 0; i < this.rowCount; i++) {
            for (int j = 0; j < this.colCount; j++) {
                if (this.seats[i][j].isOccupied() == true) {
                    num++;
                }
            }
        }
        return num;
    }
}
