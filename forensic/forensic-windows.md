# Forensic Windows

```text
$MFT = contient la liste de tous les fichiers stockés sur le disque
$LogFile = Un fichier qui contient un journal des opérations effectuées et des problèmes rencontrés par un système d'exploitation.
$Bitmap = Tableau de bits, Chaque bits indique quel cluster ils utilisent (alloué or libre pour allocation)
$BOOT = Toujours localisé au premier clusters du volume, il contient le bootstrap code (NTLDR/BOOTMGR) et le paramètres BIOS
$UpCase = Table de caractères unicode pour assurer la sensibilité à la casse dans win32 et l'espace de nom DOS
$SECURE = Base de donnée d'ACL qui réduit la surcharge en ayant plusieurs ACL identiques stockées avec chaque fichier (stockant ces ACL uniquement dans cette base de données)
$EXTEND = Dossier de FS contenant les options d'extensions variés comme $Quota, $ObjId, $Reparse or $UsnJrnl
$UsnJrnl = fichier contenant les enregistrements lorsque un changement est fait sur un fichier ou dossier
```

