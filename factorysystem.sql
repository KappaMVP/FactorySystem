-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2021-05-20 13:59:14
-- 伺服器版本： 10.4.18-MariaDB
-- PHP 版本： 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `factorysystem`
--

-- --------------------------------------------------------

--
-- 資料表結構 `face`
--

CREATE TABLE `face` (
  `EmpID` varchar(50) NOT NULL,
  `EmpName` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `identity` varchar(10) NOT NULL,
  `EnterTime` datetime(6) NOT NULL,
  `OuterTime` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `face`
--

INSERT INTO `face` (`EmpID`, `EmpName`, `identity`, `EnterTime`, `OuterTime`) VALUES
('C107156102', '呂柏佑', '作業人員', '2021-05-20 19:52:42.000000', '2021-05-20 19:53:34.000000');

-- --------------------------------------------------------

--
-- 資料表結構 `login`
--

CREATE TABLE `login` (
  `account` varchar(14) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(10) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 傾印資料表的資料 `login`
--

INSERT INTO `login` (`account`, `name`, `password`) VALUES
('a001', 'lian', 'klp'),
('a002', 'yan', '123');

-- --------------------------------------------------------

--
-- 資料表結構 `member`
--

CREATE TABLE `member` (
  `id` varchar(30) COLLATE utf8_bin NOT NULL,
  `name` varchar(30) CHARACTER SET big5 COLLATE big5_bin NOT NULL,
  `email` varchar(30) COLLATE utf8_bin NOT NULL,
  `score` int(3) NOT NULL,
  `identity` varchar(10) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- 傾印資料表的資料 `member`
--

INSERT INTO `member` (`id`, `name`, `email`, `score`, `identity`) VALUES
('C107156102', '呂柏佑', 'C107156102@nkust.edu.tw', 55, '管理人員');

-- --------------------------------------------------------

--
-- 資料表結構 `safeidentify`
--

CREATE TABLE `safeidentify` (
  `EmpID` varchar(50) NOT NULL,
  `EmpName` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ImgID` varchar(50) NOT NULL,
  `LoseTime` datetime(6) NOT NULL,
  `LoseName` varchar(50) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `LoseScore` int(50) NOT NULL,
  `TotalScore` int(50) NOT NULL DEFAULT 100,
  `ID` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `safeidentify`
--

INSERT INTO `safeidentify` (`EmpID`, `EmpName`, `ImgID`, `LoseTime`, `LoseName`, `LoseScore`, `TotalScore`, `ID`) VALUES
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:54:57.000000', 'nomask', 5, 65, 15),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:55:41.000000', 'nomask', 5, 65, 16),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:55:56.000000', 'nomask', 5, 65, 17),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:05.000000', 'nomask', 5, 65, 18),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:08.000000', 'nomask', 5, 65, 19),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:11.000000', 'nomask', 5, 65, 20),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:14.000000', 'nomask', 5, 65, 21),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:17.000000', 'nomask', 5, 65, 22),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:20.000000', 'nomask', 5, 65, 23),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:32.000000', 'nomask', 5, 65, 24),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:35.000000', 'nomask', 5, 65, 25),
('C107156102', '呂柏佑', 'C107156102_202105202nohelmet.jpg', '2021-05-20 19:56:35.000000', 'nohelmet', 10, 55, 26),
('C107156102', '呂柏佑', 'C107156102_202105202nomask.jpg', '2021-05-20 19:56:38.000000', 'nomask', 5, 55, 27);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `face`
--
ALTER TABLE `face`
  ADD PRIMARY KEY (`EnterTime`);

--
-- 資料表索引 `login`
--
ALTER TABLE `login`
  ADD UNIQUE KEY `account` (`account`);

--
-- 資料表索引 `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `safeidentify`
--
ALTER TABLE `safeidentify`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ImgID` (`ImgID`),
  ADD KEY `ImgID_2` (`ImgID`),
  ADD KEY `ImgID_3` (`ImgID`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `safeidentify`
--
ALTER TABLE `safeidentify`
  MODIFY `ID` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
