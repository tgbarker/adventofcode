import 'dart:async';
import 'dart:io';
import 'dart:convert';

const int nbRows = 128;
const int nbCols = 8;
const String frontIndicator = "F";
const String backIndicator = "B";
const String leftIndicator = "L";
const String rightIndicator = "R";

num highestId = 0;
List<int> seatIds = [];
main(List<String> args) {
  List<String> lines = new File(args[0]).readAsLinesSync();

  lines.forEach((element) {
    num seatId = analyzeSeat(element);
    if (seatId > highestId) highestId = seatId;
    seatIds.add(seatId.toInt());
  });
  print("Pt 1 : Highest ID $highestId");

  //print("SEATS : ${seatIds.toString()}");

  ///
  /// Part 2
  ///
  seatIds.sort();
  int previousDiff = 0;
  for (int i = 0; i < seatIds.length; i++) {
    if (i > 0) previousDiff = seatIds[i] - seatIds[i - 1];
    if (previousDiff > 1) {
      var mySeat = seatIds[i] - 1;
      print("Pt 2 : My Seat : $mySeat");
    }
  }
}

int analyzeSeat(String line) {
  //print(line);
  num rowSeat = 0, rowMax = 64, colSeat = 0, colMax = 4;
  for (int i = 0; i < line.length; i++) {
    var char = line[i];
    if (i <= 6) {
      if (char == backIndicator) {
        rowSeat += rowMax;
      }
      rowMax = rowMax / 2;
    } else if (i >= 7) {
      if (char == rightIndicator) {
        colSeat += colMax;
      }
      colMax = colMax / 2;
    }
  }
  num seatId = (rowSeat * 8) + colSeat;
  return seatId.toInt();
  //print("Seat number : $rowSeat:$colSeat");
}
