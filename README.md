
# Poster Generator

**Description:** This Python script generates an anime poster using the Python Imaging Library (PIL). It allows you to create custom anime posters by adding text, images, and genre information.

## Features

- Add anime series name and season number.
- Include the studio name.
- Display premiere date and episode count.
- Add a list of genres to the poster.
- Customize the poster layout and design.

## Dependencies

- Python 3.x
- Pillow (PIL Fork) library

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/anime-poster-generator.git
   ```

2. Install the required dependencies:

   ```bash
   pip install Pillow
   ```

## Usage

1. Place your anime-related images in the `image` directory.

2. Customize the poster elements by editing the `main` method in the `Poster` class.

3. Run the script to generate the anime poster:

   ```bash
   python anime_poster.py
   ```

4. The generated poster will be displayed and saved as `anime_poster.png`.

## Example

Here's an example of how to use the script:

```python
Posters = Poster()
Posters.main()
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of the Pillow library for image manipulation.
- Inspired by anime posters of various series.


