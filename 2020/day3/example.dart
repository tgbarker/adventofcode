import 'dart:async';
import 'dart:io';
import 'dart:convert';

int square = ".".codeUnitAt(0);
int tree = "#".codeUnitAt(0);
int horizontalIncrement = 3;
int horizontalPos = 3;
int treeCount = 0;
List<int> horSlopes = [1, 3, 5, 7, 1];
List<int> verSlopes = [1, 1, 1, 1, 2];

main(List<String> args) {
  List<String> lines = new File(args[0]).readAsLinesSync();
  print("Part 1 : Tree count ${trySlope(lines, 3, 1)}");

  int pt2total = trySlope(lines, 1, 1) *
      trySlope(lines, 3, 1) *
      trySlope(lines, 5, 1) *
      trySlope(lines, 7, 1) *
      trySlope(lines, 1, 2);

  print("Part 2 : Tree Count $pt2total");
}

int trySlope(
    List<String> lines, int horizontalProgression, int verticalProgression) {
  int horizontalPos = horizontalProgression;
  int treeCount = 0;
  for (int i = verticalProgression;
      i < lines.length;
      i += verticalProgression) {
    String line = lines[i];
    //print("x=$horizontalPos y=${i}");
    if (line.length <= horizontalPos) {
      horizontalPos = horizontalPos - line.length;
    }
    if (line.codeUnitAt(horizontalPos) == tree) {
      //print("Tree encountered");
      treeCount++;
    }
    horizontalPos += horizontalProgression;
    //print(lines[i]);
  }
  return treeCount;
}
