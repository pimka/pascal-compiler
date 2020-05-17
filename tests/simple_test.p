PROGRAM calc;
VAR
	j : INTEGER;
	C: Set of 0..7;
	a = array[1..5] of integer;
	function add(num : integer, num2 : integer, t2 :real) : integer;
	begin
		writeln(t2);
		add := num + num2;
	end;
BEGIN
	j := 1;
	j := add(j,2,5.0);
	if j = 1 then
		j := 2;
	WRITELN(j);
	WRITELN(1.0 / 3.0);
	WRITELN(4 div 3);
	WRITELN(5 mod 3);
END.