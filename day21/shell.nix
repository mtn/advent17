with import <nixpkgs> {};

let
  py = pkgs.python37;
in
stdenv.mkDerivation rec {
  name = "python-environment";

  buildInputs = with py.pkgs; [
    py
    py.pkgs.numpy
  ];
}

