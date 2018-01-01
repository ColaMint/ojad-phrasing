# ojad-phrasing

# Install

```sh
pip install git+https://github.com/Everley1993/ojad-phrasing.git
```

# Usage

```sh
ojad-phrasing -h
usage: ojad-phrasing [-h] [-estimation {crf,bunsetsu}] ...

ojad-phrasing

positional arguments:
  text

optional arguments:
  -h, --help            show this help message and exit
  -estimation {crf,bunsetsu}
                        アクセント句境界推定
                        crf       - 機械学習による句境界推定
                        bunsetsu  - 文節境界を利用
```

# Example

```sh
echo "日本語を勉強します。" | ojad-phrasing
　－－－－　－－－－＋
にほんごをべんきうします。
日本語を勉強します。
```

```sh
ojad-phrasing "日本語を勉強します。"
　－－－－　－－－－＋
にほんごをべんきうします。
日本語を勉強します。
```
