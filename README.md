<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BMI Calculator</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>

    <header>
        <div class="logo">
            <span>💪</span>
            <h2>FitCheck</h2>
        </div>

        <nav>
            <a href="#home">Home</a>
            <a href="#about">About BMI</a>
        </nav>
    </header>

    <main id="home">
        <section class="calculator-container">
            <h1>BMI Calculator</h1>

            <p class="description">
                Calculate your Body Mass Index and understand your weight category.
            </p>

            <div class="input-box">
                <label for="weight">Weight (kg)</label>
                <input type="number" id="weight" placeholder="Enter your weight">
            </div>

            <div class="input-box">
                <label for="height">Height (cm)</label>
                <input type="number" id="height" placeholder="Enter your height">
            </div>

            <button>Calculate BMI</button>

            <div class="result">
                <h3>Your BMI Result</h3>
                <p>Enter your details to calculate BMI.</p>
            </div>
        </section>

        <section class="bmi-info" id="about">
            <h2>What is BMI?</h2>
            <p>
                Body Mass Index (BMI) is a value calculated using a person's
                height and weight. It gives a general indication of whether a
                person's weight is within a healthy range.
            </p>

            <h3>BMI Formula</h3>
            <p><strong>BMI = Weight (kg) / Height² (m²)</strong></p>

            <div class="categories">
                <div class="category underweight">
                    <h4>Underweight</h4>
                    <p>Below 18.5</p>
                </div>

                <div class="category normal">
                    <h4>Normal Weight</h4>
                    <p>18.5 - 24.9</p>
                </div>

                <div class="category overweight">
                    <h4>Overweight</h4>
                    <p>25 - 29.9</p>
                </div>

                <div class="category obesity">
                    <h4>Obesity</h4>
                    <p>30 and above</p>
                </div>
            </div>
        </section>
    </main>

    <footer>
        <p>© 2026 BMI Calculator | Created by Ankit Verma</p>
    </footer>

</body>
</html>
