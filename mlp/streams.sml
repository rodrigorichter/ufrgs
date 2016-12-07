load "Math";
datatype 'a stream = Stream of (unit -> 'a * 'a stream);


fun geraListaInteiros 2 = []
| geraListaInteiros a = (geraListaInteiros (a-1))@(a::nil); 

fun ehPrimo (a,1) = true 
| ehPrimo a = if (a mod (a-1)) == 0 then false
	else (ehPrimo (a,(a-2)))
| ehPrimo (a,b) = if (a mod b) == 0 then false
	else (ehPrimo (a,b-1));

fun achaProximoPrimo a = if (ehPrimo a) then a
        else (achaProximoPrimo (a+1));


val PrimoStream = let
	fun primos a = Stream(fn () => (a, primos((achaProximoPrimo a))))
in
	primos 0
end;

fun NthPrimosStream 0 (Stream S) = #1 (S ())
| NthPrimosStream n (Stream S) = NthPrimosStream (n-1) (#2 (S()));

