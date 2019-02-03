Epoch Time Converter
--------------

![](https://imgur.com/LeO2ztb.gif)

This is an Alfred Workflow to help you convert between unix timestamps and human readable strings.
It is modeled after [https://www.epochconverter.com/](https://www.epochconverter.com/)

The supported calculations include:

1. **etc now** Returns the current time in UTC and as a unix timestamp
2. **etc** *unix_ts*: Given a unix timestamp in seconds, returns the equivalent time in both system local time and UTC timezone

## Build:

- Building uses the [workflow-build.py script](https://gist.github.com/AdamWagner/38228953422e830c4484e62ff116466a)
  bundled in this repo.
- To build, run: `python workflow-build.py -f -d . -o .`


## License

This Workflow is available under the terms of the MIT License. See the full
[LICENSE](LICENSE.TXT) for more details.


## Contributing

Contributions to this project are welcome. To contribute, feel free to fork
this repo, add your changes/features/improvements, then open a pull request.
Don't for get to add your name to the [AUTHORS](AUTHORS.md) file.

