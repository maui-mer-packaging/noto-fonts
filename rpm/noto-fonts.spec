%global fontname noto
%global fontconf 66-%{fontname}
%global common_desc \
Noto fonts aims to remove tofu from web by providing fonts for all \
Unicode supported script. Its design goal is to achieve visual harmonization\
between multiple scripts. Noto family supports almost all script available \
in Unicode.

Name:           noto-fonts
Version:        20140801
Release:        1%{?dist}
Summary:        Hinted and Unhinted open type fonts for Unicode scripts
Group:          User Interface/X
License:        ASL 2.0
URL:            https://code.google.com/p/noto
Source0:        %{name}-%{version}.tar.xz
Source2:        %{fontconf}-sans.conf
Source3:        %{fontconf}-sans-armenian.conf
Source4:        %{fontconf}-sans-avestan.conf
Source5:        %{fontconf}-sans-bengali.conf
Source6:        %{fontconf}-sans-bengali-ui.conf
Source7:        %{fontconf}-sans-brahmi.conf
Source8:        %{fontconf}-sans-carian.conf
Source9:        %{fontconf}-sans-cherokee.conf
Source10:        %{fontconf}-sans-coptic.conf
Source11:        %{fontconf}-sans-deseret.conf
Source12:        %{fontconf}-sans-devanagari.conf
Source13:        %{fontconf}-sans-devanagari-ui.conf
Source14:        %{fontconf}-sans-egyptian-hieroglyphs.conf
Source15:        %{fontconf}-sans-ethiopic.conf
Source16:        %{fontconf}-sans-georgian.conf
Source17:        %{fontconf}-sans-glagolitic.conf
Source18:        %{fontconf}-sans-hebrew.conf
Source19:        %{fontconf}-sans-imperial-aramaic.conf
Source20:        %{fontconf}-sans-kaithi.conf
Source21:        %{fontconf}-sans-kannada.conf
Source22:        %{fontconf}-sans-kayah-li.conf
Source23:        %{fontconf}-sans-kharoshthi.conf
Source24:        %{fontconf}-sans-khmer.conf
Source25:        %{fontconf}-sans-khmer-ui.conf
Source26:        %{fontconf}-sans-lao.conf
Source27:        %{fontconf}-sans-lao-ui.conf
Source28:        %{fontconf}-sans-lisu.conf
Source29:        %{fontconf}-sans-lycian.conf
Source30:        %{fontconf}-sans-lydian.conf
Source31:        %{fontconf}-sans-malayalam.conf
Source32:        %{fontconf}-sans-malayalam-ui.conf
Source33:        %{fontconf}-sans-mandaic.conf
Source34:        %{fontconf}-sans-meeteimayek.conf
Source35:        %{fontconf}-sans-nko.conf
Source36:        %{fontconf}-sans-old-south-arabian.conf
Source37:        %{fontconf}-sans-old-turkic.conf
Source38:        %{fontconf}-sans-osmanya.conf
Source39:        %{fontconf}-sans-phoenician.conf
Source40:        %{fontconf}-sans-shavian.conf
Source41:        %{fontconf}-sans-symbols.conf
Source42:        %{fontconf}-sans-tagalog.conf
Source43:        %{fontconf}-sans-tai-tham.conf
Source44:        %{fontconf}-sans-tamil.conf
Source45:        %{fontconf}-sans-tamil-ui.conf
Source46:        %{fontconf}-sans-telugu.conf
Source47:        %{fontconf}-sans-thai.conf
Source48:        %{fontconf}-sans-thai-ui.conf
Source49:        %{fontconf}-sans-ugaritic.conf
Source50:        %{fontconf}-sans-ui.conf
Source51:        %{fontconf}-sans-vai.conf
Source52:        %{fontconf}-serif-armenian.conf
Source53:        %{fontconf}-serif.conf
Source54:        %{fontconf}-serif-georgian.conf
Source55:        %{fontconf}-serif-khmer.conf
Source56:        %{fontconf}-serif-lao.conf
Source57:        %{fontconf}-serif-thai.conf
Source58:        %{fontconf}-sans-kannada-ui.conf
Source59:        %{fontconf}-sans-telugu-ui.conf
Source60:        %{fontconf}-sans-gujarati.conf
Source61:        %{fontconf}-sans-gujarati-ui.conf
Source62:        %{fontconf}-sans-hanunno.conf
Source63:        %{fontconf}-sans-tai-viet.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
%common_desc


%package -n %{fontname}-sans-fonts
Summary:        Free sans-serif font for Latin script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-fonts
%common_desc
Hinted sans-serif fonts for Latin script.

%_font_pkg -n sans -f %{fontconf}-sans.conf NotoSans-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-armenian-fonts
Summary:        Free sans-serif font for Armenian script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-armenian-fonts
%common_desc
Hinted sans-serif fonts for Armenian script.

%_font_pkg -n sans-armenian -f %{fontconf}-sans-armenian.conf NotoSansArmenian-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-avestan-fonts
Summary:        Free sans-serif font for Avestan script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-avestan-fonts
%common_desc
Unhinted sans-serif fonts for Avestan script.

%_font_pkg -n sans-avestan -f %{fontconf}-sans-avestan.conf NotoSansAvestan-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-bengali-fonts
Summary:        Free sans-serif font for Bengali script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-bengali-fonts
%common_desc
Unhinted sans-serif fonts for Bengali script.

%_font_pkg -n sans-bengali -f %{fontconf}-sans-bengali.conf NotoSansBengali-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-bengali-ui-fonts
Summary:        Free sans-serif UI font for Bengali script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-bengali-ui-fonts
%common_desc
Unhinted sans-serif UI fonts for Bengali script.

%_font_pkg -n sans-bengali-ui -f %{fontconf}-sans-bengali-ui.conf NotoSansBengaliUI-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-brahmi-fonts
Summary:        Free sans-serif font for Brahmi script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-brahmi-fonts
%common_desc
Unhinted sans-serif fonts for Brahmi script.

%_font_pkg -n sans-brahmi -f %{fontconf}-sans-brahmi.conf NotoSansBrahmi-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-carian-fonts
Summary:        Free sans-serif font for Carian script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-carian-fonts
%common_desc
Unhinted sans-serif fonts for Carian script.

%_font_pkg -n sans-carian -f %{fontconf}-sans-carian.conf NotoSansCarian-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-cherokee-fonts
Summary:        Free sans-serif font for Cherokee script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-cherokee-fonts
%common_desc
Unhinted sans-serif fonts for Cherokee script.

%_font_pkg -n sans-cherokee -f %{fontconf}-sans-cherokee.conf NotoSansCherokee-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-coptic-fonts
Summary:        Free sans-serif font for Coptic script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-coptic-fonts
%common_desc
Unhinted sans-serif fonts for Coptic script.

%_font_pkg -n sans-coptic -f %{fontconf}-sans-coptic.conf NotoSansCoptic-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-deseret-fonts
Summary:        Free sans-serif font for Deseret script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-deseret-fonts
%common_desc
Unhinted sans-serif fonts for Deseret script.

%_font_pkg -n sans-deseret -f %{fontconf}-sans-deseret.conf NotoSansDeseret-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-devanagari-fonts
Summary:        Free Devanagari script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-devanagari-fonts
%common_desc
Hinted sans-serif fonts for Devanagari script.

%_font_pkg -n sans-devanagari -f %{fontconf}-sans-devanagari.conf NotoSansDevanagari-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-devanagari-ui-fonts
Summary:        Free Devanagari script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-devanagari-ui-fonts
%common_desc
Hinted sans-serif UI fonts for Devanagari script.

%_font_pkg -n sans-devanagari-ui -f %{fontconf}-sans-devanagari-ui.conf NotoSansDevanagariUI-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-ethiopic-fonts
Summary:        Free Ethiopic script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-ethiopic-fonts
%common_desc
Hinted sans-serif fonts for Ethiopic script.

%_font_pkg -n sans-ethiopic -f %{fontconf}-sans-ethiopic.conf NotoSansEthiopic-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-egyptian-hieroglyphs-fonts
Summary:        Free sans-serif font for Egyptian Hieroglyphs script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-egyptian-hieroglyphs-fonts
%common_desc
Unhinted sans-serif fonts for Egyptian Hieroglyphs script.

%_font_pkg -n sans-egyptian-hieroglyphs -f %{fontconf}-sans-egyptian-hieroglyphs.conf NotoSansEgyptianHieroglyphs-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-georgian-fonts
Summary:        Free Georgian script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-georgian-fonts
%common_desc
Hinted sans-serif fonts for Georgian script.

%_font_pkg -n sans-georgian -f %{fontconf}-sans-georgian.conf NotoSansGeorgian-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-glagolitic-fonts
Summary:        Free sans-serif font for Glagolitic script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-glagolitic-fonts
%common_desc
Unhinted sans-serif fonts for Glagolitic script.

%_font_pkg -n sans-glagolitic -f %{fontconf}-sans-glagolitic.conf NotoSansGlagolitic-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-hebrew-fonts
Summary:        Free Hebrew script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-hebrew-fonts
%common_desc
Hinted sans-serif fonts for Hebrew script.

%_font_pkg -n sans-hebrew -f %{fontconf}-sans-hebrew.conf NotoSansHebrew-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-imperial-aramaic-fonts
Summary:        Free sans-serif font for Imperial Aramaic script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-imperial-aramaic-fonts
%common_desc
Unhinted sans-serif fonts for Imperial Aramaic script.

%_font_pkg -n sans-imperial-aramaic -f %{fontconf}-sans-imperial-aramaic.conf NotoSansImperialAramaic-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-kaithi-fonts
Summary:        Free sans-serif font for Kaithi script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-kaithi-fonts
%common_desc
Unhinted sans-serif fonts for Kaithi script.

%_font_pkg -n sans-kaithi -f %{fontconf}-sans-kaithi.conf NotoSansKaithi-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-kannada-fonts
Summary:        Free sans-serif font for Kannada script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-kannada-fonts
%common_desc
Unhinted sans-serif fonts for Kannada script.

%_font_pkg -n sans-kannada -f %{fontconf}-sans-kannada.conf NotoSansKannada-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-kayah-li-fonts
Summary:        Free sans-serif font for Kayah Li script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-kayah-li-fonts
%common_desc
Unhinted sans-serif fonts for Kayah Li script.

%_font_pkg -n sans-kayah-li -f %{fontconf}-sans-kayah-li.conf NotoSansKayahLi-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-kharoshthi-fonts
Summary:        Free sans-serif font for Kharoshthi script
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-kharoshthi-fonts
%common_desc
Unhinted sans-serif fonts for Kharoshthi script.

%_font_pkg -n sans-kharoshthi -f %{fontconf}-sans-kharoshthi.conf NotoSansKharoshthi-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-khmer-fonts
Summary:        Free Khmer script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-khmer-fonts
%common_desc
Hinted sans-serif fonts for Khmer script.

%_font_pkg -n sans-khmer -f %{fontconf}-sans-khmer.conf NotoSansKhmer-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-khmer-ui-fonts
Summary:        Free Khmer script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-khmer-ui-fonts
%common_desc
Hinted sans-serif UI fonts for Khmer script.

%_font_pkg -n sans-khmer-ui -f %{fontconf}-sans-khmer-ui.conf NotoSansKhmerUI-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-lao-fonts
Summary:        Free Lao script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-lao-fonts
%common_desc
Hinted sans-serif fonts for Lao script.

%_font_pkg -n sans-lao -f %{fontconf}-sans-lao.conf NotoSansLao-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-lao-ui-fonts
Summary:        Free Lao script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-lao-ui-fonts
%common_desc
Hinted sans-serif UI fonts for Lao script.

%_font_pkg -n sans-lao-ui -f %{fontconf}-sans-lao-ui.conf NotoSansLaoUI-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-lisu-fonts
Summary:        Free Lisu script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-lisu-fonts
%common_desc
Unhinted sans-serif UI fonts for Lisu script.

%_font_pkg -n sans-lisu -f %{fontconf}-sans-lisu.conf NotoSansLisu-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-lycian-fonts
Summary:        Free Lycian script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-lycian-fonts
%common_desc
Unhinted sans-serif UI fonts for Lycian script.

%_font_pkg -n sans-lycian -f %{fontconf}-sans-lycian.conf NotoSansLycian-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-lydian-fonts
Summary:        Free Lydian script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-lydian-fonts
%common_desc
Unhinted sans-serif UI fonts for Lydian script.

%_font_pkg -n sans-lydian -f %{fontconf}-sans-lydian.conf NotoSansLydian-*.ttf
%doc LICENSE



%package -n %{fontname}-sans-malayalam-fonts
Summary:        Free Malayalam script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-malayalam-fonts
%common_desc
Unhinted sans-serif fonts for Malayalam script.

%_font_pkg -n sans-malayalam -f %{fontconf}-sans-malayalam.conf NotoSansMalayalam*.ttf
%doc LICENSE


%package -n %{fontname}-sans-malayalam-ui-fonts
Summary:        Free Malayalam script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-malayalam-ui-fonts
%common_desc
Unhinted sans-serif UI fonts for Malayalam script.

%_font_pkg -n sans-malayalam-ui -f %{fontconf}-sans-malayalam-ui.conf NotoSansMalayalamUI*.ttf
%doc LICENSE


%package -n %{fontname}-sans-mandaic-fonts
Summary:        Free Mandaic script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-mandaic-fonts
%common_desc
Unhinted sans-serif fonts for Mandaic script.

%_font_pkg -n sans-mandaic -f %{fontconf}-sans-mandaic.conf NotoSansMandaic*.ttf
%doc LICENSE


%package -n %{fontname}-sans-meeteimayek-fonts
Summary:        Free Meetei Mayek script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-meeteimayek-fonts
%common_desc
Unhinted sans-serif fonts for Meetei Mayek script.

%_font_pkg -n sans-meeteimayek -f %{fontconf}-sans-meeteimayek.conf NotoSansMeeteiMayek*.ttf
%doc LICENSE

%package -n %{fontname}-sans-nko-fonts
Summary:        Free NKo script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-nko-fonts
%common_desc
Unhinted sans-serif fonts for NKo script.

%_font_pkg -n sans-nko -f %{fontconf}-sans-nko.conf NotoSansNKo*.ttf
%doc LICENSE


%package -n %{fontname}-sans-old-south-arabian-fonts
Summary:        Free Old South Arabian script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-old-south-arabian-fonts
%common_desc
Unhinted sans-serif fonts for Old South Arabian script.

%_font_pkg -n sans-old-south-arabian -f %{fontconf}-sans-old-south-arabian.conf NotoSansOldSouthArabian*.ttf
%doc LICENSE


%package -n %{fontname}-sans-old-turkic-fonts
Summary:        Free Old Turkic script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-old-turkic-fonts
%common_desc
Unhinted sans-serif fonts for Old Turkic script.

%_font_pkg -n sans-old-turkic -f %{fontconf}-sans-old-turkic.conf NotoSansOldTurkic*.ttf
%doc LICENSE


%package -n %{fontname}-sans-osmanya-fonts
Summary:        Free Osmanya script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-osmanya-fonts
%common_desc
Unhinted sans-serif fonts for Osmanya script.

%_font_pkg -n sans-osmanya -f %{fontconf}-sans-osmanya.conf NotoSansOsmanya*.ttf
%doc LICENSE


%package -n %{fontname}-sans-phoenician-fonts
Summary:        Free Phoenician script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-phoenician-fonts
%common_desc
Unhinted sans-serif fonts for Phoenician script.

%_font_pkg -n sans-phoenician -f %{fontconf}-sans-phoenician.conf NotoSansPhoenician*.ttf
%doc LICENSE



%package -n %{fontname}-sans-shavian-fonts
Summary:        Free Shavian script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-shavian-fonts
%common_desc
Unhinted sans-serif fonts for Shavian script.

%_font_pkg -n sans-shavian -f %{fontconf}-sans-shavian.conf NotoSansShavian*.ttf
%doc LICENSE


%package -n %{fontname}-sans-symbols-fonts
Summary:        Free Symbols script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-symbols-fonts
%common_desc
Unhinted sans-serif fonts for Symbols script.

%_font_pkg -n sans-symbols -f %{fontconf}-sans-symbols.conf NotoSansSymbols*.ttf
%doc LICENSE



%package -n %{fontname}-sans-tagalog-fonts
Summary:        Free tagalog script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-tagalog-fonts
%common_desc
Unhinted sans-serif fonts for tagalog script.

%_font_pkg -n sans-tagalog -f %{fontconf}-sans-tagalog.conf NotoSansTagalog*.ttf
%doc LICENSE


%package -n %{fontname}-sans-tai-tham-fonts
Summary:        Free Tai Tham script sans-serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-tai-tham-fonts
%common_desc
Unhinted sans-serif fonts for Tai Tham script.

%_font_pkg -n sans-tai-tham -f %{fontconf}-sans-tai-tham.conf NotoSansTaiTham*.ttf
%doc LICENSE


%package -n %{fontname}-sans-tamil-fonts
Summary:        Free Tamil script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-tamil-fonts
%common_desc
Hinted sans-serif fonts for Tamil script.

%_font_pkg -n sans-tamil -f %{fontconf}-sans-tamil.conf NotoSansTamil-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-tamil-ui-fonts
Summary:        Free Tamil script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-tamil-ui-fonts
%common_desc
Hinted sans-serif UI fonts for Tamil script.

%_font_pkg -n sans-tamil-ui -f %{fontconf}-sans-tamil-ui.conf NotoSansTamilUI-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-telugu-fonts
Summary:        Free Telugu script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-telugu-fonts
%common_desc
Unhinted sans-serif fonts for Telugu script.

%_font_pkg -n sans-telugu -f %{fontconf}-sans-telugu.conf NotoSansTelugu-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-thai-fonts
Summary:        Free Thai script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-thai-fonts
%common_desc
Hinted sans-serif fonts for Thai script.

%_font_pkg -n sans-thai -f %{fontconf}-sans-thai.conf NotoSansThai-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-thai-ui-fonts
Summary:        Free Thai script sans-serif fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-thai-ui-fonts
%common_desc
Hinted sans-serif UI fonts for Thai script.

%_font_pkg -n sans-thai-ui -f %{fontconf}-sans-thai-ui.conf NotoSansThaiUI-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-ugaritic-fonts
Summary:        Free Ugaritic script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-ugaritic-fonts
%common_desc
Unhinted sans-serif fonts for Ugaritic script.

%_font_pkg -n sans-ugaritic -f %{fontconf}-sans-ugaritic.conf NotoSansUgaritic-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-ui-fonts
Summary:        Free sans-serif Latin script fonts for UI
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-ui-fonts
%common_desc
Hinted sans-serif UI fonts for Latin script.

%_font_pkg -n sans-ui -f %{fontconf}-sans-ui.conf NotoSansUI-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-vai-fonts
Summary:        Free Vai script sans-serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-vai-fonts
%common_desc
Unhinted sans-serif fonts for Vai script.

%_font_pkg -n sans-vai -f %{fontconf}-sans-vai.conf NotoSansVai-*.ttf
%doc LICENSE



%package -n %{fontname}-serif-armenian-fonts
Summary:        Free Armenian script serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-serif-armenian-fonts
%common_desc
Hinted serif fonts for Armenian script.

%_font_pkg -n serif-armenian -f %{fontconf}-serif-armenian.conf NotoSerifArmenian*.ttf
%doc LICENSE

%package -n %{fontname}-serif-fonts
Summary:        Free Latin script serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-serif-fonts
%common_desc
Hinted serif fonts for Latin script.

%_font_pkg -n serif -f %{fontconf}-serif.conf NotoSerif-**.ttf
%doc LICENSE

%package -n %{fontname}-serif-georgian-fonts
Summary:        Free Georgian script serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-serif-georgian-fonts
%common_desc
Hinted serif fonts for Georgian script.

%_font_pkg -n serif-georgian -f %{fontconf}-serif-georgian.conf NotoSerifGeorgian*.ttf
%doc LICENSE

%package -n %{fontname}-serif-khmer-fonts
Summary:        Free Khmer script serif font
Requires:       fontpackages-filesystem

%description -n %{fontname}-serif-khmer-fonts
%common_desc
Hinted serif fonts for Khmer script.

%_font_pkg -n serif-khmer -f %{fontconf}-serif-khmer.conf NotoSerifKhmer-*.ttf
%doc LICENSE

%package -n %{fontname}-serif-lao-fonts
Summary:        Free Lao script serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-serif-lao-fonts
%common_desc
Hinted serif fonts for Lao script.

%_font_pkg -n serif-lao -f %{fontconf}-serif-lao.conf NotoSerifLao*.ttf
%doc LICENSE


%package -n %{fontname}-serif-thai-fonts
Summary:        Free Thai script serif fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-serif-thai-fonts
%common_desc
Hinted serif fonts for Thai script.

%_font_pkg -n serif-thai -f %{fontconf}-serif-thai.conf NotoSerifThai*.ttf
%doc LICENSE


%package -n %{fontname}-sans-kannada-ui-fonts
Summary:        Free Unhinted Kannada script sans fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-kannada-ui-fonts
%common_desc
Unhinted sanserif UI fonts for Kannada script.

%_font_pkg -n sans-kannada-ui -f %{fontconf}-sans-kannada-ui.conf NotoSansKannadaUI*.ttf
%doc LICENSE

%package -n %{fontname}-sans-telugu-ui-fonts
Summary:        Free Unhinted Telugu script sans fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-telugu-ui-fonts
%common_desc
Unhinted sanserif UI fonts for Telugu script.

%_font_pkg -n sans-telugu-ui -f %{fontconf}-sans-telugu-ui.conf NotoSansTeluguUI*.ttf
%doc LICENSE


%package -n %{fontname}-sans-gujarati-fonts
Summary:        Free Unhinted Gujarati script sans fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-gujarati-fonts
%common_desc
Unhinted sanserif fonts for Gujarati script.

%_font_pkg -n sans-gujarati -f %{fontconf}-sans-gujarati.conf NotoSansGujarati-*.ttf
%doc LICENSE

%package -n %{fontname}-sans-gujarati-ui-fonts
Summary:        Free Unhinted Gujarati script sans UI fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-gujarati-ui-fonts
%common_desc
Unhinted sanserif UI fonts for Gujarati script.

%_font_pkg -n sans-gujarati-ui -f %{fontconf}-sans-gujarati-ui.conf NotoSansGujaratiUI*.ttf
%doc LICENSE


%package -n %{fontname}-sans-hanunno-fonts
Summary:        Free Unhinted Hanunno script sans fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-hanunno-fonts
%common_desc
Unhinted sanserif fonts for Hanunno script.

%_font_pkg -n sans-hanunno -f %{fontconf}-sans-hanunno.conf NotoSansHanunoo-*.ttf
%doc LICENSE


%package -n %{fontname}-sans-tai-viet-fonts
Summary:        Free Unhinted Tai Viet script sans fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-sans-tai-viet-fonts
%common_desc
Unhinted sanserif fonts for Tai Viet script.

%_font_pkg -n sans-tai-viet -f %{fontconf}-sans-tai-viet.conf NotoSansTaiViet*.ttf
%doc LICENSE

%prep
%setup -q -n %{name}-%{version}/upstream
rm -rf fonts/individual/hinted/*{Cham,Kufi,Gurmukhi}*
rm -rf fonts/individual/hinted/{Arimo,Cousine,Tinos}*
cp -p fonts/individual/hinted/*.ttf .
rm -rf fonts/individual/unhinted/*{Khmer,Lao,Hebrew,Kufi,Naskh,Balinese,Bamum,Batak,Buginese,Buhid,Canadian,Cham}*
rm -rf fonts/individual/unhinted/*{Cypriot,Gothic,Gurmukhi,Javanese,Lepcha,Limbu,LinearB,Mongolian,Myanmar}*
rm -rf fonts/individual/unhinted/*{NewTaiLue,Ogham,OlChiki,OldItalic,OldPersian,Pahlavi,Parthian,PhagsPa,Rejang}*
rm -rf fonts/individual/unhinted/*{Runic,Samaritan,Saurashtra,Sinhala,SumeroAkkadianCuneiform,Sundanese}*
rm -rf fonts/individual/unhinted/*{SylotiNagri,Syriac,Tagbanwa,TaiLe,Tifinagh,Yi}*
cp -p fonts/individual/unhinted/*.ttf .

%build

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-armenian.conf
install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-avestan.conf
install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-bengali.conf
install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-bengali-ui.conf
install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-brahmi.conf
install -m 0644 -p %{SOURCE8} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-carian.conf
install -m 0644 -p %{SOURCE9} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-cherokee.conf
install -m 0644 -p %{SOURCE10} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-coptic.conf
install -m 0644 -p %{SOURCE11} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-deseret.conf
install -m 0644 -p %{SOURCE12} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari.conf
install -m 0644 -p %{SOURCE13} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-devanagari-ui.conf
install -m 0644 -p %{SOURCE14} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-egyptian-hieroglyphs.conf
install -m 0644 -p %{SOURCE15} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-ethiopic.conf
install -m 0644 -p %{SOURCE16} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-georgian.conf
install -m 0644 -p %{SOURCE17} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-glagolitic.conf
install -m 0644 -p %{SOURCE18} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-hebrew.conf
install -m 0644 -p %{SOURCE19} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-imperial-aramaic.conf
install -m 0644 -p %{SOURCE20} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kaithi.conf
install -m 0644 -p %{SOURCE21} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kannada.conf
install -m 0644 -p %{SOURCE22} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kayah-li.conf
install -m 0644 -p %{SOURCE23} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kharoshthi.conf
install -m 0644 -p %{SOURCE24} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-khmer.conf
install -m 0644 -p %{SOURCE25} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-khmer-ui.conf
install -m 0644 -p %{SOURCE26} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lao.conf
install -m 0644 -p %{SOURCE27} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lao-ui.conf
install -m 0644 -p %{SOURCE28} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lisu.conf
install -m 0644 -p %{SOURCE29} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lycian.conf
install -m 0644 -p %{SOURCE30} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-lydian.conf
install -m 0644 -p %{SOURCE31} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-malayalam.conf
install -m 0644 -p %{SOURCE32} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-malayalam-ui.conf
install -m 0644 -p %{SOURCE33} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-mandaic.conf
install -m 0644 -p %{SOURCE34} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-meeteimayek.conf
install -m 0644 -p %{SOURCE35} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-nko.conf
install -m 0644 -p %{SOURCE36} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-old-south-arabian.conf
install -m 0644 -p %{SOURCE37} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-old-turkic.conf
install -m 0644 -p %{SOURCE38} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-osmanya.conf
install -m 0644 -p %{SOURCE39} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-phoenician.conf
install -m 0644 -p %{SOURCE40} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-shavian.conf
install -m 0644 -p %{SOURCE41} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-symbols.conf
install -m 0644 -p %{SOURCE42} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tagalog.conf
install -m 0644 -p %{SOURCE43} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tai-tham.conf
install -m 0644 -p %{SOURCE44} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tamil.conf
install -m 0644 -p %{SOURCE45} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tamil-ui.conf
install -m 0644 -p %{SOURCE46} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-telugu.conf
install -m 0644 -p %{SOURCE47} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-thai.conf
install -m 0644 -p %{SOURCE48} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-thai-ui.conf
install -m 0644 -p %{SOURCE49} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-ugaritic.conf
install -m 0644 -p %{SOURCE50} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-ui.conf
install -m 0644 -p %{SOURCE51} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-vai.conf
install -m 0644 -p %{SOURCE52} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-armenian.conf
install -m 0644 -p %{SOURCE53} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif.conf
install -m 0644 -p %{SOURCE54} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-georgian.conf
install -m 0644 -p %{SOURCE55} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-khmer.conf
install -m 0644 -p %{SOURCE56} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-lao.conf
install -m 0644 -p %{SOURCE57} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-serif-thai.conf
install -m 0644 -p %{SOURCE58} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-kannada-ui.conf
install -m 0644 -p %{SOURCE59} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-telugu-ui.conf
install -m 0644 -p %{SOURCE60} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-gujarati.conf
install -m 0644 -p %{SOURCE61} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-gujarati-ui.conf
install -m 0644 -p %{SOURCE62} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-hanunno.conf
install -m 0644 -p %{SOURCE63} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans-tai-viet.conf


for fconf in %{fontconf}-sans.conf \
             %{fontconf}-sans-armenian.conf \
             %{fontconf}-sans-avestan.conf \
             %{fontconf}-sans-bengali.conf \
             %{fontconf}-sans-bengali-ui.conf \
             %{fontconf}-sans-brahmi.conf \
             %{fontconf}-sans-carian.conf \
             %{fontconf}-sans-cherokee.conf \
             %{fontconf}-sans-coptic.conf \
             %{fontconf}-sans-deseret.conf \
             %{fontconf}-sans-devanagari.conf \
             %{fontconf}-sans-devanagari-ui.conf \
             %{fontconf}-sans-egyptian-hieroglyphs.conf \
             %{fontconf}-sans-ethiopic.conf \
             %{fontconf}-sans-georgian.conf \
             %{fontconf}-sans-glagolitic.conf \
             %{fontconf}-sans-hebrew.conf \
             %{fontconf}-sans-imperial-aramaic.conf \
             %{fontconf}-sans-kaithi.conf \
             %{fontconf}-sans-kannada.conf \
             %{fontconf}-sans-kayah-li.conf \
             %{fontconf}-sans-kharoshthi.conf \
             %{fontconf}-sans-khmer.conf \
             %{fontconf}-sans-khmer-ui.conf \
             %{fontconf}-sans-lao.conf \
             %{fontconf}-sans-lao-ui.conf \
             %{fontconf}-sans-lisu.conf \
             %{fontconf}-sans-lycian.conf \
             %{fontconf}-sans-lydian.conf \
             %{fontconf}-sans-malayalam.conf \
             %{fontconf}-sans-malayalam-ui.conf \
             %{fontconf}-sans-mandaic.conf \
             %{fontconf}-sans-meeteimayek.conf \
             %{fontconf}-sans-nko.conf \
             %{fontconf}-sans-old-south-arabian.conf \
             %{fontconf}-sans-old-turkic.conf \
             %{fontconf}-sans-osmanya.conf \
             %{fontconf}-sans-phoenician.conf \
             %{fontconf}-sans-shavian.conf \
             %{fontconf}-sans-symbols.conf \
             %{fontconf}-sans-tagalog.conf \
             %{fontconf}-sans-tai-tham.conf \
             %{fontconf}-sans-tamil.conf \
             %{fontconf}-sans-tamil-ui.conf \
             %{fontconf}-sans-telugu.conf \
             %{fontconf}-sans-thai.conf \
             %{fontconf}-sans-thai-ui.conf \
             %{fontconf}-sans-ugaritic.conf \
             %{fontconf}-sans-ui.conf \
             %{fontconf}-sans-vai.conf \
             %{fontconf}-serif-armenian.conf \
             %{fontconf}-serif.conf \
             %{fontconf}-serif-georgian.conf \
             %{fontconf}-serif-khmer.conf \
             %{fontconf}-serif-lao.conf \
             %{fontconf}-sans-kannada-ui.conf \
             %{fontconf}-sans-telugu-ui.conf \
             %{fontconf}-serif-thai.conf \
             %{fontconf}-sans-gujarati.conf \
             %{fontconf}-sans-gujarati-ui.conf \
             %{fontconf}-sans-hanunno.conf \
             %{fontconf}-sans-tai-viet.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%clean
rm -fr %{buildroot}
