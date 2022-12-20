// Link to the Question - https://edabit.com/challenge/o7TwicAHWuMkjbDqQ

function whichIsLarger(f, g) {
	if (f()> g()){
		return "f"
	}
	else if (f()< g()){
		return "g"
	}
	else {
		return "neither"
	}
}