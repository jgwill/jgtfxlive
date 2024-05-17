kill $(ps -aef|grep jgtfxl|grep python|grep config|grep fxlive|awk '//{print $2}');fg

